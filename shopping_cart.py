import datetime
import sys


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
    return f"${my_price:,.2f}"

def two_dec(my_price):
    return f"{my_price:,.2f}"

#1) capture product ID and put it in a list

selected_ids_list = []
id_range = range(1, 20)
id_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

#x=1
#if x not in id_range:
#    print("NOOOOt in range")
#else:
#    print("In range")

while True:

    selected_id = input("Please select a product ID from 1 to 20 or type DONE ")
    #if selected_id != 
    #if selected_id not in id_range:
     #   print ("INVALID PRODUCT ID. PLEASE TRY AGAIN")
    if selected_id.upper() == "DONE":
        print("HERE IS YOUR RECEIPT:")
        break
    elif int(selected_id) not in id_list:
        print(selected_id, "IS AN INVALID PRODUCT ID. PLEASE TRY AGAIN")
        sys.exit()
    else:
        selected_ids_list.append(selected_id)
    print(selected_id)

#print(selected_ids_list)
#print the receipt:

print("---------------------------------------")
print("EVE'S APPLE GROCERY STORE")
print("EMAIL: EVESAPPLESTORE")

print("---------------------------------------")
print("CHECKOUT AT:", datetime.datetime.now())

print("---------------------------------------")
print("SELECTED PRODUCTS:")

subtotal = 0
for sel_id in selected_ids_list:
    matching_products = [p for p in products if str(p["id"]) == str(sel_id)]
    matching_product = matching_products[0]
    subtotal = subtotal + matching_product["price"]
    print("---", matching_product["name"], to_usd(matching_product["price"]))
    
print("---------------------------------------")
tax = subtotal*0.0875
total = subtotal+tax
print("SUBTOTAL:", to_usd(subtotal))
print("TAX:", to_usd(tax))
print("TOTAL:", to_usd(total))
    
print("---------------------------------------")
print("THANK YOU! SEE YOU SOON!")
print("---------------------------------------")


#2)look up product prices for each product on the list
#3) calculate totals 
#4) print a receipt 
#5) ask for an email
#6) close the transaction