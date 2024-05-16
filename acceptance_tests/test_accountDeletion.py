from django.test import TestCase
from django.urls import reverse
from project_app.models import User
from django.test import Client

class TestAccountDeletion(TestCase):

    def setUp(self):
        # Create a user with a unique email address for testing
        User.objects.create(userID='test_user1', password='test_password', email='test_delete@example.com',
                            phone='1234567890', address='123 Test St', role='Admin', firstName='Test',
                            lastName='User')

    def test_delete_user_success(self):
        # Create a client to simulate a user interacting with the website
        client = Client()

        # Attempt to delete the user
        response = client.post(reverse('deleteUser'), {
            'userID': 'test_user1'
        })

        print(response.status_code)
        print(User.objects.filter(userID='test_user1').exists())

        # Check that the response is a success
        self.assertEqual(response.status_code, 302)

        # Check that the user was actually deleted
        self.assertFalse(User.objects.filter(userID='test_user1').exists())
