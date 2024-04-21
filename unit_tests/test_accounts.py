import unittest
from TA_Assigner.models import User

class AccountTestCase(unittest.TestCase):
    def setUp(self):
        self.setUser = User()

    def testDefaultUser(self):
        assert self.setUser.userID == 'admin'
        assert self.setUser.password == 'admin'
        assert self.setUser.email is None
        assert self.setUser.phone == 0
        assert self.setUser.address is None
        assert self.setUser.firstName == 'first'
        assert self.setUser.lastName == 'last'
        assert self.setUser.role == 'TA'

