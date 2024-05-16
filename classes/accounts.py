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
        try:
            self.validate_phone(str(self.phone))  # Convert to string to ensure length check works
        except ValueError as e:
            return str(e)  # Return the error message if validation fails

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

    def edit_user(self, user, **kwargs):
        for key, value in kwargs.items():
            if hasattr(User, key):
                setattr(user, key, value)
            else:
                raise AttributeError(f"Attribute '{key}' does not exist in Account")

    def set_email(self, email):
        try:
            self.validate_email(email)
            self.email = email
        except ValueError as e:
            print(f"Email validation failed: {e}")
            raise

    def set_phone(self, phone):
        try:
            self.validate_phone(phone)
            self.phone = phone
        except ValueError as e:
            raise ValueError(str(e))

    def validate_email(self, email):
        if '@' not in email or '.' not in email:
            raise ValueError("Invalid email format")

    def validate_phone(self, phone):
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Phone number must be a 10-digit number")

    def validate_role(self, role):
        VALID_ROLES = ['Admin', 'Supervisor', 'Tester', 'TA']
        if role not in VALID_ROLES:
            raise ValueError("Invalid role")
