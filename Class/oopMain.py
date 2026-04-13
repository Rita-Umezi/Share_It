# inheritance syntax
class Faculty:
    def __init__(self, department, population):
        # These attributes belong to the parent class.
        self.department = department
        self.population = population

    def display(self):
        # This method displays the general faculty information.
        print(f"Department: {self.department}, Population: {self.population}")

class Dept(Faculty):
    def __init__(self, department, population, name, student_population):
        # super() calls the parent class constructor so inherited
        # attributes are created for this child object.
        super().__init__(department, population)

        # These attributes are specific to the Dept class.
        self.name = name
        self.student_population = student_population
        
    def display_faculty(self):
        # This method displays the child class information.
        print(f"Department Name: {self.name}, Student Population: {self.student_population}")
        
# Create an object from the child class.
software = Dept("Computing", 5000, "Software", 1200)

# Call each method directly because the methods already print their output.
software.display()
software.display_faculty()

"""----------------------------------------------------------------------------------"""
#BELOW IS WHAT THE LECTURER DID, SIMPLER VERSION OF WHAT I DID ABOVE
# class Faculty:
#     def __init__(self, department, population):
#         self.department = department
#         self.population = population

#     def display(self):
#         print(f"Department: {self.department}, Population: {self.population}")
        
# computing=Faculty(3,5000)

# class Department(Faculty):
#     def __init__(self, name, studentpopulation):
#         self.name = name
#         self.studentpopulation = studentpopulation

#     def display_faculty(self):
#         print(f"Department Name: {self.name}, Student Population: {self.studentpopulation}")

# Software = Department("Software engineering", 1200)
# Software.display_faculty()
# computing.display()
""""------------------------------------------------------------------------------------"""
#a simple example of inheritance in python
class Animal:
        def __init__(self, name):
            self.name= name
        
        def speak(self):
            print(f"{self.name} makes a sound.")
            
class Dog(Animal):
    pass

dog=Dog("Buddy")
print(dog.speak())

""""------------------------------------------------------------------------------------"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class Lecturer(Person):
    def __init__()        