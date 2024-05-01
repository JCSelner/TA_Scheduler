from django.test import TestCase
from unittest.mock import patch
from project_app.models import User
from classes.accounts import Account

class AccountTestCase(TestCase):

    @patch('project_app.models.User.objects.create')
    def test_save_details(self, mock_create):
        account = Account(userID='test_user', password='test_pass', email='test@example.com',
                          phone='1234567890', firstName='Test', lastName='User', role='Tester',
                          address='123 Test St.')
        mock_create.return_value = User(userID='test_user', password='test_pass', email='test@example.com',
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
        self.assertEqual(account.email, None)
        self.assertEqual(account.phone, 0)
        self.assertEqual(account.firstName, 'first')
        self.assertEqual(account.lastName, 'last')
        self.assertEqual(account.role, 'TA')
        self.assertEqual(account.address, None)

    def test_edit_user(self):
        account = Account()
        account.edit_user(firstName='New', lastName='User', email='new@example.com')
        self.assertEqual(account.firstName, 'New')
        self.assertEqual(account.lastName, 'User')
        self.assertEqual(account.email, 'new@example.com')

    def test_edit_user_invalid_attribute(self):
        account = Account()
        with self.assertRaises(AttributeError):
            account.edit_user(invalid_attribute='value')

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            account = Account(email='invalid_email')

    def test_invalid_phone_number(self):
        with self.assertRaises(ValueError):
            account = Account(phone='invalid_phone_number')

    def test_invalid_role(self):
        with self.assertRaises(ValueError):
            account = Account(role='invalid_role')
