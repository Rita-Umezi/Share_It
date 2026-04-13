# Create a Python class named Investment with attributes to store the investment 
# account name, investment number, initial value of the investment, current 
# value, administration charges, and profit. Include a method named 
# calculate_profit() that computes the profit as the difference between the current 
# value and the initial value, minus the administration charges. 
# Next, create another class named HouseInvestment that inherits from the 
# Investment class. This class should include an additional attribute to store the 
# investment duration. Also, include a method named calculate_percent_profit() 
# that calculates the percentage profit by dividing the profit by the initial value. 
# Finally, write a Python program that creates an object of the HouseInvestment 
# class and displays the following details: investment account name, investment 
# number, initial value, investment duration, current value, profit, and percentage 
# profit. 

class Investment:
    def __init__(self, account_name, investment_number, initial_value, current_value, admin_charges):
        self.account_name = account_name
        self.investment_number = investment_number
        self.initial_value = initial_value
        self.current_value = current_value
        self.admin_charges = admin_charges
        self.profit = 0

    def calculate_profit(self):
        self.profit = (self.current_value - self.initial_value) - self.admin_charges
        return self.profit


class HouseInvestment(Investment):
    def __init__(self, account_name, investment_number, initial_value, current_value, admin_charges, duration):
        super().__init__(account_name, investment_number, initial_value, current_value, admin_charges)
        self.duration = duration  # in years

    def calculate_percent_profit(self):
        # Ensure profit is calculated first
        if self.profit == 0:
            self.calculate_profit()
        
        percent_profit = (self.profit / self.initial_value) * 100
        return percent_profit


# Main program
account_name = input("Enter account name: ")
investment_number = input("Enter investment number: ")
initial_value = float(input("Enter initial value: "))
current_value = float(input("Enter current value: "))
admin_charges = float(input("Enter administration charges: "))
duration = float(input("Enter investment duration (years): "))

# Create object
investment = HouseInvestment(account_name, investment_number, initial_value, current_value, admin_charges, duration)

# Calculate values
profit = investment.calculate_profit()
percent_profit = investment.calculate_percent_profit()

# Display results
print("\nInvestment Details")
print("Account Name:", investment.account_name)
print("Investment Number:", investment.investment_number)
print("Initial Value:", investment.initial_value)
print("Duration (years):", investment.duration)
print("Current Value:", investment.current_value)
print("Profit:", profit)
print("Percentage Profit:", percent_profit, "%")