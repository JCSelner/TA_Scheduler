from django.test import TestCase
from unittest.mock import patch, MagicMock
from classes.accounts import Account
from django.urls import reverse
from django.test import Client
from project_app.models import User

class AccountTestCase(TestCase):

    @patch('project_app.models.User.objects.create')
    def test_save_details_success(self, mock_create):
        user_mock = MagicMock()
        user_mock.userID = 'test_user'
        user_mock.firstName = 'Test'
        user_mock.lastName = 'User'
        user_mock.email = 'test@example.com'
        user_mock.phone = '1234567890'
        user_mock.role = 'Tester'
        user_mock.address = '123 Test St.'
        mock_create.return_value = user_mock

        account = Account(userID='test_user', password='test_pass', email='test@example.com',
                          phone='1234567890', firstName='Test', lastName='User', role='Tester',
                          address='123 Test St.')

        result = account.save_details()
        self.assertEqual(result, "Test User with ID test_user saved to the db")
        mock_create.assert_called_once_with(userID='test_user', password='test_pass', email='test@example.com',
                                            phone='1234567890', firstName='Test', lastName='User', role='Tester',
                                            address='123 Test St.')

    def test_delete_user(self):
        account = Account(userID='test_user', password='test_pass', email='test@example.com',
                          phone='1234567890', firstName='Test', lastName='User', role='Tester',
                          address='123 Test St.')
        account.delete_user()
        self.assertEqual(account.userID, 'admin')
        self.assertEqual(account.password, 'admin')
        self.assertIsNone(account.email)
        self.assertEqual(account.phone, 0)
        self.assertEqual(account.firstName, 'first')
        self.assertEqual(account.lastName, 'last')
        self.assertEqual(account.role, 'TA')
        self.assertIsNone(account.address)

    def test_edit_user(self):
        # Assuming edit_user.html is accessible at '/editUser/<pk>/'
        user = User.objects.create(userID='test_user', password='test_pass', email='test@example.com',
                                    phone='1234567890', firstName='Test', lastName='User', role='Tester',
                                    address='123 Test St.')
        client = Client()
        response = client.get(reverse('editUser', kwargs={'pk': user.pk}))
        self.assertEqual(response.status_code, 302)

    def test_invalid_email(self):
        account = Account()
        with self.assertRaises(ValueError):
            account.set_email('invalid_email')

    def test_invalid_phone_number(self):
        account = Account()
        with self.assertRaises(ValueError):
            account.set_phone('invalid_phone_number')

    def test_invalid_role(self):
        account = Account()
        with self.assertRaises(ValueError):
            account.validate_role('invalid_role')

    def test_edit_user_invalid_attribute(self):
        account = Account()
        user = User.objects.create(userID='test_user', password='test_pass', email='test@example.com',
                                   phone='1234567890', firstName='Test', lastName='User', role='Tester',
                                   address='123 Test St.')
        with self.assertRaises(AttributeError):
            account.edit_user(user, invalid_attribute='value')
            user.save()

    def test_edit_user_form_submission(self):
        user = User.objects.create(userID='test_user', password='test_pass', email='test@example.com',
                                    phone='1234567890', firstName='Test', lastName='User', role='Tester',
                                    address='123 Test St.')
        client = Client()
        response = client.post(reverse('editUser', kwargs={'pk': user.pk}), {
            'email': 'new_email@example.com',
            'phone': '9876543210',
            'role': 'NewRole',
            'address': '456 New St.'
        })
        updated_user = User.objects.get(pk=user.pk)
        self.assertEqual(updated_user.email, 'new_email@example.com')
        self.assertEqual(updated_user.phone, '9876543210')
        self.assertEqual(updated_user.role, 'NewRole')
        self.assertEqual(updated_user.address, '456 New St.')




