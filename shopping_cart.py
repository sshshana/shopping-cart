# shopping_cart.py

# Import all the modules and third-party packages that contain the functionality we need:
# We want to allow users choose their own tax rate by creating a separate virtual environment

import os
from dotenv import load_dotenv 

load_dotenv() # this one happens to read env vars from the ".env" file (read README.md)
tax_rate = float(os.getenv("tax_rate", default=8.75))/100 # uses the os module to read the specified environment variable and store it in a corresponding python variable

# import a module to print the date and time on the receipt
from datetime import datetime

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


print("-------------------")
print("Let's scan some items. Once you finish scanning, please enter DONE.")
print("-------------------")

my_cart = [] # scanned items will be stored in this list variable

def scanning():
    # input the identifier of each shopping cart item
    scanned_item = input(f"Please input a product identifier.")
    if scanned_item == "DONE":
        # complete the check out and display store info
        print("---------------------------------")
        print("MAGNIFICENT GROCERY")
        print("WWW.MAGNIFICENTGROCERY.COM")
        print("PHONE: 123-214-0818")
        print("---------------------------------")
    else:
        # validate the input
        matching_item = [ item for item in products if str(item["id"]) == scanned_item ]
        if len(matching_item) == 0: # if there is nothing that matches with the selected id, print the error message
            print("Hey, are you sure that product identifier is correct? Please try again!")
        else:
            my_cart.append(matching_item[0])
            matching_item = [] # initialize the variable
        
        scanning() # loop the process

scanning()

# print the date
print("CHECKOUT AT:", datetime.now().strftime("%b %d, %Y %H:%M:%S"))
print("---------------------------------")

# print the scanned items
print("SELECTED PRODUCTS:")

for item in my_cart:
    print("+ ", item["name"], "(", to_usd(item["price"]), ")")

print("---------------------------------")

# calculate and print the subtotal, tax, and total
subtotal = 0
for item in my_cart:
    subtotal = subtotal + item["price"]

tax = subtotal * tax_rate
total = subtotal + tax

print("SUBTOTAL:", to_usd(subtotal))
print(f"TAX: {to_usd(tax)} (sales tax rate: {tax_rate*100}%)")
print("TOTAL:", to_usd(total))
print("---------------------------------")

# thank you message
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")