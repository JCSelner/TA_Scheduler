from TA_Assigner.models import User
class Account(object):
    def __init__(self, userID='admin', password='admin', email=None, phone=0, firstName='first',
                 lastName='last', role='TA', address=None):
        self.userID = userID
        self.password = password
        self.email = email
        self.phone = phone
        self.firstName = firstName
        self.lastName = lastName
        self.role = role
        self.address = address

    def createUser(self, other):
        pass

    def deleteUser(self):
        pass

    def editUserPassword(self, other):
        pass

    def editUserID(self, other):
        pass

    def editUserEmail(self, other):
        pass

    def editUserPhoneNumber(self, other):
        pass

    def editUserAddress(self, other):
        pass

    def editUserFirstName(self, other):
        pass

    def editUserLastName(self, other):
        pass

    def editUserRole(self, other):
        pass
