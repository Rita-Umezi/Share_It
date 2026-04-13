# Question 4: Employee Record System

# Create a class called Employee with:

# Instance variables: name, salary

# Class variable: company_name

# Tasks:

# Create at least 3 employees

# Write a setter that increases salary (e.g., add bonus)

# Write a getter to display salary

# Display all employee details

class Employee:
    company_name = "Tech Solutions Inc."  # Class variable shared by all instances

    def __init__(self, name, salary):
        self.name = name  # Instance variable for the employee's name
        self._salary = salary  # Instance variable for the employee's salary (protected)

    @property
    def salary(self):
        return self._salary  # Getter method to retrieve the salary

    @salary.setter
    def salary(self, bonus):
        if bonus >= 0:  # Validate that the bonus is not negative
            self._salary += bonus  # Setter method to increase the salary by adding a bonus
        else:
            print("Bonus cannot be negative.")  # Handle negative bonus
# Create at least 3 employees
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)
employee3 = Employee("Charlie", 55000)
# Display all employee details
employees = [employee1, employee2, employee3]
for employee in employees:
    print(f"Name: {employee.name}, Salary: {employee.salary}, Company: {Employee.company_name}")
# Increase salary for employee1 by adding a bonus
employee1.salary = 5000  # Valid bonus
print(f"Updated Employee: {employee1.name}, Salary: {employee1.salary}, Company: {Employee.company_name}")
employee1.salary = -1000  # Invalid bonus, should print an error message
print(f"Attempted Invalid Update: {employee1.name}, Salary: {employee1.salary}, Company: {Employee.company_name}")
    