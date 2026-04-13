# Write an OOP program in Python that defines a base class named Calculation 
# with methods to perform addition and subtraction. Create a derived class named 
# AdvancedCalculation that inherits from Calculation and adds methods for 
# multiplication and division. The program should perform all operations and 
# display the results.

class Calculation:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2


class AdvancedCalculation(Calculation):
    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            return "Division by zero is not allowed."
        return num1 / num2


calculator = AdvancedCalculation()

first_number = 20
second_number = 5

print("Addition:", calculator.add(first_number, second_number))
print("Subtraction:", calculator.subtract(first_number, second_number))
print("Multiplication:", calculator.multiply(first_number, second_number))
print("Division:", calculator.divide(first_number, second_number))
