"""
product inventory system: a store keeps track of products and their quantities
allow the user to add a new product
allow the user to update the quantity of an existing product
display all products and quantities
"""
inventory = {
    "apple": 50,
    "banana": 100,
    "orange": 75
}
# Function to add a new product
def add_product(product_name, quantity):
    if product_name in inventory:
        print(f"{product_name} already exists in the inventory.")
    else:
        inventory[product_name] = quantity
        print(f"{product_name} added to the inventory with quantity {quantity}.")
        
# Function to update the quantity of an existing product
def update_quantity(product_name, quantity):
    if product_name in inventory:
        inventory[product_name] = quantity
        print(f"{product_name} quantity updated to {quantity}.")
    else:
        print(f"{product_name} does not exist in the inventory.")
        
# Function to display all products and quantities
def display_inventory():
    print("Current Inventory:")
    for product, quantity in inventory.items():
        print(f"{product}: {quantity}")
# Example usage
add_product("grape", 30) 
update_quantity("apple", 60)
display_inventory()