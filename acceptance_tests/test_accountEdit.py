from django.test import TestCase
from django.urls import reverse
from project_app.models import User
from django.test import Client

class TestAccountEdit(TestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create(userID='test_user1', password='test_password', email='test_edit@example.com',
                            phone='1234567890', address='123 Test St', role='Admin', firstName='Test',
                            lastName='User')

    def test_edit_user_success(self):
        # Create a client to simulate a user interacting with the website
        client = Client()

        # Attempt to edit the user's information
        response = client.post(reverse('editUser', kwargs={'pk': self.user.pk}), {
            'email': 'edited_email@example.com',
            'phone': '9876543210',
            'role': 'Instructor',
            'address': '456 Edit St',
        })

        # Check that the response is a redirect (indicating success)
        self.assertEqual(response.status_code, 200)

        # Refresh the user instance from the database to get the updated information
        self.user.refresh_from_db()

        # Check that the user's information was updated correctly
        self.assertEqual(self.user.email, 'edited_email@example.com')
        self.assertEqual(self.user.phone, '9876543210')
        self.assertEqual(self.user.role, 'Instructor')
        self.assertEqual(self.user.address, '456 Edit St')

    def test_edit_user_failure(self):
        # Create a client to simulate a user interacting with the website
        client = Client()

        # Attempt to edit the user's information with invalid data
        response = client.post(reverse('editUser', kwargs={'pk': self.user.pk}), {
            'email': 'invalid_email',
            'phone': '1234567890',
            'role': 'InvalidRole',
            'address': '123 Test St',
        })

        # Check that the response is not a redirect (indicating failure)
        self.assertNotEqual(response.status_code, 302)

        # Refresh the user instance from the database to ensure no changes were made
        self.user.refresh_from_db()

        # Check that the user's information remains unchanged
        self.assertNotEqual(self.user.email, 'invalid_email')
        self.assertNotEqual(self.user.role, 'InvalidRole')

