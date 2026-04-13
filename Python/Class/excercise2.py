age=input("Enter your age: ")
age=int(age)#converts to integer

if age>=0 and age<=12:
    print("Child")
elif age>=13 and age<=19:
    print("Teenager")
elif age>=20 and age<=59:
    print("Adult")
else:
    print("Senior Citizen")


#multiple if example below
#if more than one condition is true is when multiple if statements are used
toppings=["Mushrooms", "Pepperoni", "Cheese"]
if "Mushrooms" in toppings:
    print("Adding mushrooms")
if "Pepperoni" in toppings:
    print("Adding pepperonis")
if "Cheese" in toppings:
    print("Adding cheese")

"""
write a program that checks if a username is available
INSTRUCTIONS
Store an existing username in a variable
Ask the user to enter a new username
Comapre both usernames without considering case

if the username already exists, print a warning. Otherwise, print that the username is available
"""

username="Rita"
InputUser=input("Enter a new username: ")
if InputUser.lower() == username.lower():
    print("Warning: Username already exists")
else:
    print("Username is available")
       