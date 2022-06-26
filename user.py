# user_name, user_number, user_email, user_address, user_password

class user:

    def __init__(self, user_name, user_number, user_email, user_address, user_password):
        self.user_name = user_name
        self.user_number = user_number
        self.user_email = user_email
        self.user_address = user_address
        self.user_password = user_password

    def __str__(self):
        return f"User Name : {self.user_name} \nUser Number : {self.user_number} \nUser Email : {self.user_email} \nUser Address : {self.user_address} \nUser Password : {self.user_password}"

    def set_user_name(self,user_name):
        self.user_name = user_name

    def get_user_name(self):
        return self.user_name

    def set_user_number(self,user_number):
        self.user_number = user_number

    def get_user_number(self):
        return self.user_number

    def set_user_email(self,user_email):
        self.user_email = user_email

    def get_user_email(self):
        return self.user_email

    def set_user_address(self,user_address):
        self.user_address = user_address

    def get_user_address(self):
        return self.user_address

    def set_user_password(self,user_password):
        self.user_password = user_password

    def get_user_password(self):
        return self.user_password
