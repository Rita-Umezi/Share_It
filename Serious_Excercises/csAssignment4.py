# Write an OOP program in Python that defines a base class named Account with 
# attributes such as account number and balance. Create a derived class named 
# SavingsAccount that inherits from Account and includes an interest rate. The 
# program should include a method to calculate and display the new balance after 
# adding interest.

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate  # in percentage

    def add_interest(self):
        interest = (self.interest_rate / 100) * self.balance
        self.balance += interest
        return self.balance


# Main program
account_number = input("Enter account number: ")
balance = float(input("Enter balance: "))
interest_rate = float(input("Enter interest rate (%): "))

# Create SavingsAccount object
savings = SavingsAccount(account_number, balance, interest_rate)

# Calculate and display new balance
new_balance = savings.add_interest()

print("\nAccount Number:", savings.account_number)
print("Balance after adding interest:", new_balance)