import unittest
from classes.accounts import Account


class TestAccount(unittest.TestCase):

    def setUp(self):
        self.account = Account()

    def test_default_values(self):
        self.assertEqual(self.account.userID, 'admin')
        self.assertEqual(self.account.password, 'admin')
        self.assertIsNone(self.account.email)
        self.assertEqual(self.account.phone, 0)
        self.assertEqual(self.account.firstName, 'first')
        self.assertEqual(self.account.lastName, 'last')
        self.assertEqual(self.account.role, 'TA')
        self.assertIsNone(self.account.address)

    def test_create_user(self):
        other = Account(userID='user1', password='pass1', email='user1@example.com')
        self.account.createUser(other)
        self.assertEqual(self.account.userID, 'user1')
        self.assertEqual(self.account.password, 'pass1')
        self.assertEqual(self.account.email, 'user1@example.com')

    def test_delete_user(self):
        # Create a user
        self.account = Account(userID='user1', password='pass1', email='user1@example.com')
        self.account.deleteUser()
        # Assert that all fields are reset to default values
        self.assertEqual(self.account.userID, 'admin')
        self.assertEqual(self.account.password, 'admin')
        self.assertIsNone(self.account.email)
        self.assertEqual(self.account.phone, 0)
        self.assertEqual(self.account.firstName, 'first')
        self.assertEqual(self.account.lastName, 'last')
        self.assertEqual(self.account.role, 'TA')
        self.assertIsNone(self.account.address)

    def test_edit_user_password(self):
        self.account.editUserPassword('new_password')
        self.assertEqual(self.account.password, 'new_password')

    def test_edit_user_id(self):
        self.account.editUserID('new_user_id')
        self.assertEqual(self.account.userID, 'new_user_id')

    def test_edit_user_email(self):
        self.account.editUserEmail('new_email@example.com')
        self.assertEqual(self.account.email, 'new_email@example.com')

    def test_edit_user_phone_number(self):
        self.account.editUserPhoneNumber('1234567890')
        self.assertEqual(self.account.phone, '1234567890')

    def test_edit_user_address(self):
        self.account.editUserAddress('123 Main St')
        self.assertEqual(self.account.address, '123 Main St')

    def test_edit_user_first_name(self):
        self.account.editUserFirstName('John')
        self.assertEqual(self.account.firstName, 'John')

    def test_edit_user_last_name(self):
        self.account.editUserLastName('Doe')
        self.assertEqual(self.account.lastName, 'Doe')

    def test_edit_user_role(self):
        self.account.editUserRole('Instructor')
        self.assertEqual(self.account.role, 'Instructor')


if __name__ == '__main__':
    unittest.main()
