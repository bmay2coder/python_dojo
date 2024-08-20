# Lecture 1

class User:		
    def __init__(self):
        self.first_name = "Ada"
        self.last_name = "Lovelace"
        self.age = 42
# Now that you have a class set up with a constructor 
# You can assign new variables to new users in the outer scope!
user_ada = User()
print(user_ada.first_name) # prints Ada

# Create another user called user_2!
# Print user_ada's last name.
# Print user_2's last name. (Yes, they should be the same)
# Run the code, pause, go back and step through one line at a time
# What do you notice about the order it runs in?
# Write down any other questions you have.
# Sensei Exercise: try just printing the variable, user_ada.
#   What prints to the terminal?

# class Shoe:
#     # now our method has 4 parameters (including self)!
#     def __init__(self, brand, shoe_type, price):
#     	# we assign them accordingly
#         self.brand = brand
#         self.type = shoe_type
#         self.price = price
#     	# the status is set to True by default
#         self.in_stock = True
# skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
# dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
# print(skater_shoe.type)	# output: Low-top Trainers
# print(dress_shoe.type)	# output: Ballet Flats

# class User:		# here's what we have so far
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#     # adding the greeting method
#     def greeting(self):
#     	print(f"Hello, my name is {self.name}")

# adrien = User("Adrien", "adion@codingdojo.com")
# cool_person = User("Sadie", "sflick@codingdojo.com")

# adrien.greeting()
# cool_person.greeting()

# class Shoe:

#     def __init__(self, brand, shoe_type, price):
#         self.brand = brand
#         self.type = shoe_type
#         self.price = price
#         self.in_stock = True
    
#     # Takes a float/percent as an argument and reduces the
#     # price of the item by that percentage.
#     def on_sale_by_percent(self, percent_off):
#         self.price = self.price * (1-percent_off)
    
#     # Returns a total with tax added to the price.
#     def total_with_tax(self, tax_rate):
#         tax = self.price * tax_rate
#         total = self.price + tax
#         return total
    
#     # Reduces the price by a fixed dollar amount.
#     def cut_price_by(self, amount):
#         if amount < self.price:
#             self.price -= amount
#         else:
#             print("Price deduction too large.")

# # Create some shoes. Call some methods on those shoes. Print your shoe's attributes..
# my_shoe = Shoe("Converse", "Low-tops", 36.00)
# print(my_shoe.total_with_tax(0.05))
# my_shoe.cut_price_by(10)
# print(my_shoe.price)


# Lecture 2

# class BankAccount:
#     # Declaring a class attribute
#     # Shared among all bank accounts
#     bank_name = "First National Dojo"		
    
#     def __init__(self, int_rate, balance):
#         self.int_rate = int_rate
#         self.balance = balance

# adriens_account = BankAccount(.001, 5000)
# sadies_account = BankAccount(.01, 10000)
# adriens_account.bank_name = "Dojo Credit Union"
    
# print(adriens_account.bank_name)
# # output: Dojo Credit Union
    
# print(sadies_account.bank_name)
# # output: First National Dojo

# BankAccount.bank_name = "Bank of Dojo"
    
# print(adriens_account.bank_name)
# # output: Bank of Dojo
    
# print(sadies_account.bank_name)
# # output: Bank of Dojo

# class Player:
#     def __init__(self, name, age, position, team):
#         self.name = name
#         self.age = age
#         self.position = position
#         self.team = team

# kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}
     
# # Pass in all the values from the dictionary by their keys
# player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
# print(player_kevin.position)


# Lecture 3