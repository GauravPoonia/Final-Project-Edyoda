# add the user before giving the choices remember it
# make dict of food list in admins
# choice removal inn users
from user import *


class user_profile():

    user_details = []
    

    def execute(self,choice):

        if choice == 1:
            print("****************** ADD USER DETAILS ******************")
            user_name = input("Enter Full Name of User : ")
            user_number = int(input("Enter Mobile Number : "))
            user_email = input("Enter a Email Id : ")
            user_address = input("Enter the full address : ")
            user_password = input("Enter a 8 digit password : ")
            user_obj = user(user_name, user_number, user_email, user_address, user_password)
            self.user_details.append(user_obj)


        elif choice == 2:
            user_cart = []
            print("****************** LOGIN TO THE APPLICATION ******************")
            email = input("Enter User Email Id : ")
            password = input("Enter User Password : ")
            for users in self.user_details:
                if users.user_email == email and users.user_password == password:
                    print("********** Yeah!! Great Your Login is Successfull **********")
                    while True:
                        print("Enter Any Choice from these : \n1. Place New Order \n2. Order History \n3. Update Profile")
                        new_choice = int(input("Enter Choice Here : "))
                        if new_choice == 1:
                            print("******************* Place An order ********************")
                            print("These items are Present In Restaurant : ")
                            items_list = {1 : "Tandoori Chicken (4 pieces) [INR 240]",
                                        2 : "Vegan Burger (1 Piece) [INR 320]", 
                                        3 :"Truffle Cake (500gm) [INR 900]"
                                        }
                            print(items_list)

                            no_of_foods = int(input("Enter the number of food items to select : "))

                            for i in range(no_of_foods):
                                add = int(input("Enter the food choice : "))
                                c = items_list[add]
                                user_cart.append(c)
                            
                            print("Selected List Of Foods Is :",user_cart)
                            print("Press Y to place the order or N to not place the order : ")
                            order_choice = input("Enter the choice Y/N : ")
                            if order_choice == "Y":
                                print("******** Yeah!! Your Order is Succesfully Placed ********")
                            elif order_choice == "N":
                                print("******** Your order is not Placed ********")
                            else:
                                print("******* Enter Y/N for order placing *******")
                                order_choice = input("Enter the choice Y/N : ")
                                if order_choice == "Y":
                                    print("******** Yeah!! Your Order is Succesfully Placed ********")
                                elif order_choice == "N":
                                    print("******** Your order is not Placed ********")
                            

                        elif new_choice == 2:
                            print("******************* Order History ******************")
                            print("************** Previous Orders ****************")
                            print(user_cart)


                        elif new_choice == 3:
                            print("****************** UPDATE USER DETAILS ******************")
                            for users in self.user_details:
                                users.set_user_name(input("Enter The New Name : "))
                                users.set_user_number(input("Enter The Mobile Number : "))
                                users.set_user_email(input("Enter The New Email : "))
                                users.set_user_address(input("Enter The New Address : "))
                                users.set_user_password(input("Enter The New Password : "))
                                print("***************** CONGRATULATIONS!! YOUR DETAILS ARE UPDATED ******************")


                else:
                    print("*********** OOPS!! Inncorrect Email and Password ***********")
                    print("******************** PLEASE TRY AGAIN ********************")


                    
        else:
            print("##################### PLEASE ENTER A VALID CHOICE #####################")


while True:
    print("************ Please Add user before Login to the Application ************* \n1. Add User \n2. Login To The Application")
    choice = int(input("Enter The Choice : "))

    user_profile_obj = user_profile()
    user_profile_obj.execute(choice)
    