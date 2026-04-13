# Create a class called Product with:

# Instance variables: name, price, quantity

# Class variable: store_name

# Tasks:

# Create 3 products

# Write a method to calculate total value (price × quantity)

# Use a setter to update price

# Use a getter to display product details

class Product:
    store_name = "Tech Store"  # Class variable shared by all instances

    def __init__(self, name, price, quantity):
        self.name = name  # Instance variable for the product name
        self._price = price  # Instance variable for the product price (protected)
        self.quantity = quantity  # Instance variable for the product quantity

    @property
    def price(self):
        return self._price  # Getter method to retrieve the price

    @price.setter
    def price(self, value):
        if value >= 0:  # Validate that the price is not negative
            self._price = value  # Setter method to update the price
        else:
            print("Price cannot be negative.")

    def total_value(self):
        return self.price * self.quantity  # Method to calculate total value
# Create 3 products
product1 = Product("Laptop", 1000, 5)
product2 = Product("Smartphone", 500, 10)
product3 = Product("Headphones", 100, 20)

# Display product details and total value for each product
products = [product1, product2, product3]
for product in products:
    print(f"Product: {product.name}, Price: {product.price}, Quantity: {product.quantity}, Total Value: {product.total_value()}, Store: {Product.store_name}")
# Update the price for product1
product1.price = 1200  # Valid update
product1.price = -100  # Invalid update, should print an error message
print(f"Updated Product: {product1.name}, Price: {product1.price}, Quantity: {product1.quantity}, Total Value: {product1.total_value()}, Store: {Product.store_name}")

