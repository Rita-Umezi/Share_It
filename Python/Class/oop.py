class car:
    def __init__(self, name, model, color, year):
        self.name = name
        self.model = model
        self.color = color
        self.year = year

    def display(self):
        print(f" The car is {self.name}, the model is {self.model}, it is {self.color} and was made in {self.year}")
car1 = car("Toyota", "Camry", "Red", 2020)
car2 = car("Honda", "Civic", "Blue", 2019)
car3 = car("Ford", "Mustang", "Black", 2021)

car1.display()
car2.display()
car3.display()
""""------------------------------------------------------------------------------------------------------------------------------"""

#Student class that takes the attributes, name, matric numeber, age and level, and they input the values, calculate their cgpa using the *args and **kwargs, and display the result using a method in the class.
class Student:
    def __init__(self, name, matric_number, age, level):
        self.name = name
        self.matric_number = matric_number
        self.age = age
        self.level = level
        
    def display(self):
        print(f"Name: {self.name}, Matric Number: {self.matric_number}, Age: {self.age}, Level: {self.level}")
    
    
name =input("Enter your name: ")
matric_number = input("Enter your matric number: ")
age = input("Enter your age: ")
level = input("Enter your level: ")

student1 = Student(name, matric_number, age, level)

student1.display()
