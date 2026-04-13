"""
shopping list application, create a simple shopping list application that allows a user to enter items into a list,
remove items and then displays the list of items.
"""
shopping_list=[]
item=int(input("Enter number of items: "))
for i in range(item):
    item_name=input("Enter item name: ")
    shopping_list.append(item_name)
print(shopping_list)

remove_item=input("Enter item to remove: ")
shopping_list.remove(remove_item)
print(shopping_list)
