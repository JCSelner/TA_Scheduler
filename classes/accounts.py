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
        self.userID = other.userID
        self.password = other.password
        self.email = other.email
        self.phone = other.phone
        self.firstName = other.firstName
        self.lastName = other.lastName
        self.role = other.role
        self.address = other.address

    def deleteUser(self):
        self.userID = 'admin'
        self.password = 'admin'
        self.email = None
        self.phone = 0
        self.firstName = 'first'
        self.lastName = 'last'
        self.role = 'TA'
        self.address = None

    def editUserPassword(self, other):
        self.password = other

    def editUserID(self, other):
        self.userID = other

    def editUserEmail(self, other):
        self.email = other

    def editUserPhoneNumber(self, other):
        self.phone = other

    def editUserAddress(self, other):
        self.address = other

    def editUserFirstName(self, other):
        self.firstName = other

    def editUserLastName(self, other):
        self.lastName = other

    def editUserRole(self, other):
        self.role = other
