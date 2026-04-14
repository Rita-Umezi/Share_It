# Write an OOP program in Python that defines a base class named Calculation 
# with methods to perform addition and subtraction. Create a derived class named 
# AdvancedCalculation that inherits from Calculation and adds methods for 
# multiplication and division. The program should perform all operations and 
# display the results.

class Calculation:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2


class AdvancedCalculation(Calculation):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Division by zero is not allowed."
        
    def display_results(self):
        print("Addition:", self.add())
        print("Subtraction:", self.subtract())
        print("Multiplication:", self.multiply())
        print("Division:", self.divide())
        
# Main program
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
calculation = AdvancedCalculation(num1, num2)
calculation.display_results()    
