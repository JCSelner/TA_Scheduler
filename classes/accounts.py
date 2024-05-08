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
        self.userID = 'admin'
        self.password = 'admin'
        self.email = None
        self.phone = 0
        self.firstName = 'first'
        self.lastName = 'last'
        self.role = 'TA'
        self.address = None

    def edit_user(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                if key == 'email':
                    self.set_email(value)
                elif key == 'phone':
                    self.set_phone(value)
                elif key == 'role':
                    self.validate_role(value)
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)
            else:
                raise AttributeError(f"Attribute '{key}' does not exist in Account")

    def set_email(self, email):
        if self.validate_email(email) != ValueError:
            self.email = email
        else:
            raise ValueError

    def set_phone(self, phone):
        self.validate_phone(phone)
        self.phone = phone

    def validate_email(self, email):
        if '@' not in email or '.' not in email:
            raise ValueError("Invalid email format")

    def validate_phone(self, phone):
        if not phone.isdigit():
            raise ValueError("Phone number must contain only digits")

    def validate_role(self, role):
        VALID_ROLES = ['Admin', 'Supervisor', 'Tester', 'TA']
        if role not in VALID_ROLES:
            raise ValueError("Invalid role")
