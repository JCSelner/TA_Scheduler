from project_app.models import User


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

    def save_details(self):
        account = User.objects.create(userID=self.userID, password=self.password,
                                      email=self.email, phone=self.phone, firstName=self.firstName,
                                      lastName=self.lastName, role=self.role, address=self.address)
        return f"{account.firstName} {account.lastName} with ID {account.userID} saved to the db"

    def delete_user(self):
        # Reset attributes to default values
        self.__init__()

    def edit_user(self, **kwargs):
        # goes through each passed in attribute and edits them through the for loop
        for key, value in kwargs.items():
            try:
                setattr(self, key, value)
            except AttributeError:
                raise AttributeError
