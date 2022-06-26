
from food_app import *

class food_project:

    food_list = []
    
    def display(self,choice):

        if choice == 1:
            print("****************** ADD FOOD ITEMS *********************")
            food_id = int(input("Enter the ID number : "))
            food_name = input("Enter the food name : ")
            food_price = float(input("Enter the food price in rupees : "))
            food_quantity = (input("Enter the food quantity : "))
            food_discount = float(input("Enter the food discount in rupees: "))
            food_stock = (input("Enter the food stock which is left : "))
            
            food_obj = food(food_id,food_name,food_quantity,food_price,food_discount,food_stock)
            self.food_list.append(food_obj)


        elif choice == 2:
            print("***************** EDIT FOOD ITEMS ********************")
            id = int(input("Enter the food Id you want : "))
            for foods in self.food_list:
                if foods.food_id == id:
                    foods.set_food_name(input("Enter the food name : "))
                    foods.set_food_price(input("Enter the food price : "))
                    foods.set_food_quantity(input("Enter the food quantity : "))
                    foods.set_food_discount(input("Enter the food discount : "))
                    foods.set_food_stock(input("Enter the food stock : "))
                print("************ Food Items Succefully Updated ***************")


        elif choice == 3:
            print("*****************Display Food*****************")
            for i in range(len(self.food_list)):
                print(self.food_list[i])
                
            
        elif choice == 4:
            print("************** REMOVE ITEMS *****************")
            food_id = int(input("Enter The food id you want to remove : "))
            for foods in self.food_list:
                if foods.food_id == food_id:
                    self.food_list.remove(foods)


        else:
            print("Wrong choice")


# while True:
#     print("************ Enter any one Choice from the following ************ :\n1. Add Food \n2. Edit Food \n3. Display Food \n4. Remove Food")
#     choice = int(input("Enter your choice : "))

#     food_project_obj = food_project()
#     food_project_obj.display(choice)
