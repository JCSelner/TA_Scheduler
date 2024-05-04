from django.test import TestCase
from unittest.mock import patch, MagicMock
from classes.accounts import Account

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
