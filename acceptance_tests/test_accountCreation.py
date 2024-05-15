from django.test import TestCase
from django.urls import reverse
from project_app.models import User
from django.test import Client

class TestAccountCreation(TestCase):

    def test_create_user_success(self):
        # Create a client to simulate a user interacting with the website
        client = Client()

        # Attempt to create a user with valid data
        response = client.post(reverse('createUser'), {
            'userID': 'test_user1',
            'password': 'test_password',
            'email': 'test@example.com',
            'phone': '1234567890',
            'address': '123 Test St',
            'role': 'Admin',
            'firstName': 'Test',
            'lastName': 'User'
        })

        # Check that the response is a redirect (indicating success)
        self.assertEqual(response.status_code, 200)

        # Check that the user was actually created
        self.assertTrue(User.objects.filter(userID='test_user1').exists())

    def test_create_user_failure(self):
        # Create a client to simulate a user interacting with the website
        client = Client()

        # Attempt to create a user with invalid data
        response = client.post(reverse('createUser'), {
            'userID': 'test_user2',
            'password': 'test_password',
            'email': 'invalid_email',
            'phone': '1234567890',
            'address': '123 Test St',
            'role': 'Admin',
            'firstName': 'Test',
            'lastName': 'User'
        })

        # Check that the response is a redirect (indicating a failure)
        self.assertEqual(response.status_code, 200)

        # Check that the user was not actually created
        self.assertFalse(User.objects.filter(userID='test_user2').exists())

    def test_create_user_invalid_phone(self):
        # Create a client to simulate a user interacting with the website
        client = Client()

        # Attempt to create a user with an invalid phone number
        response = client.post(reverse('createUser'), {
            'userID': 'test_user3',
            'password': 'test_password',
            'email': 'test@example.com',
            'phone': '12345',  # Invalid phone number
            'address': '123 Test St',
            'role': 'Admin',
            'firstName': 'Test',
            'lastName': 'User'
        })

        # Check that the response is a redirect (indicating a failure)
        self.assertEqual(response.status_code, 200)

        # Check that the user was not actually created
        self.assertFalse(User.objects.filter(userID='test_user3').exists())


