

from admin import *
from food_project import *




class admin_profile():

    admin_list = []

    def show(self,choice):

        if choice == 1:
            print("************** Admin Profile *************")
            admin_email = input("Enter your Email Id : ")
            admin_number = int(input("Enter your Mobile Number : "))
            admin_password = input("Enter your Password : ")

            admin_obj = admin(admin_email, admin_number, admin_password)

            self.admin_list.append(admin_obj)

        elif choice == 2:
            print("************ Please Login First *************")
            email_id = input("Enter Admin email id : ")
            password = input("Enter Admin password : ")
            for admins in self.admin_list:
                if admins.admin_email == email_id and admins.admin_password == password:
                    print("Successfully Login!!!")

                    while True:
                        print("************ Enter any one Choice from the following ************ :\n1. Add Food \n2. Edit Food \n3. Display Food \n4. Remove Food")
                        choice = int(input("Enter your choice : "))

                        food_project_obj = food_project()
                        food_project_obj.display(choice)

                else:
                    print("Login Failed!!!")
                    print("Please try again!!!")
        


        else:
            print("Enter a Valid Choice")

while True:
    print("Enter the choice from the following : \n1. Admin Profile : \n2. Food Items : ")
    choice = int(input("Enter the choice : "))

    admin_profile_obj = admin_profile()
    admin_profile_obj.show(choice)
