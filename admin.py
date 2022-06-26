class admin:

    def __init__(self,admin_email,admin_number,admin_password):
        self.admin_email = admin_email
        self.admin_number = admin_number
        self.admin_password = admin_password

    def __str__(self):
        return f"Admin Email : {self.admin_email} \nAdmin Number : {self.admin_number} \nAdmin Password : {self.admin_password}"

    def set_admin_email(self,admin_email):
        self.admin_email = admin_email

    def get_admin_email(self):
        return self.admin_email

    def set_admin_number(self,admin_number):
        self.admin_number = admin_number

    def get_admin_number(self):
        return self.admin_number

    def set_admin_password(self,admin_password):
        self.admin_password = admin_password

    def get_admin_password(self):
        return self.admin_password
