class Lecturer:
    def __init__(self, name, department, staff_id):
        self.name= name
        self.department= department
        self.staff_id= staff_id
        
    def display(self):
        print(f"Name: {self.name}, Department: {self.department}, Staff ID: {self.staff_id}")
        
name = input("Enter your name: ")
department = input("Enter your department: ")
staff_id = input("Enter your staff ID: ")

lecturer1 = Lecturer(name, department, staff_id)
lecturer1.display()