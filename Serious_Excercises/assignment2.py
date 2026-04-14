# Create a class called BankAccount with:

# Instance variables: account_name, balance

# Class variable: bank_name

# Tasks:

# Create 2 account objects

# Write a setter to update the balance

# Write a getter to display the balance

# Prevent setting a negative balance

class BankAccount:
    bank_name = "Global Bank"  # Class variable shared by all instances

    def __init__(self, account_name, balance):
        self.account_name = account_name  # Instance variable for the account name
        self.__balance = balance  # Instance variable for the account balance (protected)

    @property
    def balance(self):
        return self.__balance  # Getter method to retrieve the balance

    @balance.setter
    def balance(self, value):
        if value >= 0:  # Validate that the balance is not negative
            self.__balance = value  # Setter method to update the balance
        else:
            print("Balance cannot be negative.")
            
# Create 2 account objects
account1 = BankAccount("Alice's Account", 1000)
account2 = BankAccount("Bob's Account", 500)

# Display the balance for each account
print(f"{account1.account_name} Balance: {account1.balance}, Bank: {BankAccount.bank_name}")
print(f"{account2.account_name} Balance: {account2.balance}, Bank: {BankAccount.bank_name}")
# Update the balance for account1
account1.balance = 1200  # Valid update
account1.balance = -500  # Invalid update, should print an error message
print(f"{account1.account_name} Updated Balance: {account1.balance}, Bank: {BankAccount.bank_name}")
