# Question 6 
# Write an OOP program in Python that creates a base class named Person with 
# attributes such as name and age. Create a derived class named Teacher that 
# inherits from Person and adds attributes such as subject and salary. The 
# program should display all the details of the teacher. 


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Person):
    def __init__(self, name, age, subject, salary):
        super().__init__(name, age)
        self.subject = subject
        self.salary = salary

    def display_details(self):
        print("Teacher Details")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)
        print("Salary:", self.salary)


teacher1 = Teacher("Mrs. Johnson", 35, "Mathematics", 85000)
teacher1.display_details()
