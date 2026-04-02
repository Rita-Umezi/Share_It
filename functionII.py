"""
local variable: is declared inside a function and cannot be accessible outside
global variable: is declared outside all functions and is accessible anywhere in the program
"""
#usage of global variable
count=0

def increase():
    global count
    count+=1
    
increase()
print(count) 

#using positional arguments
def sum(a,b):
    return a+b
print(sum(3,4))

#using keyword arguments. When calling position of arguments does not matter
def student(fname,age,lname):
    print(f"First Name: {fname}, Age: {age}, Last Name: {lname}")
    
student(fname="Rita", age=19, lname="Smith")
student(age=19, fname="Rita", lname="Smith") 

#Arbitrary arguements
def sum(*args):
    total=0
    for num in args:
        total+=num
    return total
print(sum(1,2,3,4,5))

#Arbitrary keyword arguments
def student(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")    
student(name="Rita", age=19, city="New York")

#Lambda function
square = lambda x: x**2
print(square(5))
