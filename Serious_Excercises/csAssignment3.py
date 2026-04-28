# Question 3 
# 3(a). Create a Python class named BankAccount with attributes for an account 
# number, the owner’s name, and the account balance. Include a constructor 
# (__init__ method) that initializes each attribute to appropriate default values. 
# Also include methods to get and set the values of each attribute. Add a method 
# named deduct_monthly_fee() that reduces the account balance by $4.00. In 
# addition, include a static method named explain_account_policy() that explains 
# that a $4 service fee will be deducted from the account each month.

class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self._account_number = account_number
        self._owner_name = owner_name
        self._balance = balance

    # Getter and Setter for account_number
    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        self._account_number = value

    # Getter and Setter for owner_name
    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value

    # Getter and Setter for balance
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    # Method to deduct monthly fee
    def deduct_monthly_fee(self):
        self._balance -= 4.00

    # Static method to explain account policy
    @staticmethod
    def explain_account_policy():
        print("A $4.00 service fee will be deducted from your account every month.")


# Example usage
account = BankAccount("123456", "Ria", 100.0)

print("Account Number:", account.account_number)
print("Owner Name:", account.owner_name)
print("Balance before fee:", account.balance)

account.deduct_monthly_fee()

print("Balance after fee:", account.balance)

BankAccount.explain_account_policy()
"""------------------------------------------------------------------------------------------------"""
# 3(b). 
# Write a Python program that creates four BankAccount objects. Define a function 
# named get_data() that prompts the user to enter values for the account number, 
# owner’s name, and balance, then returns a BankAccount object with those 
# values. Call this function three times to initialize three of the accounts. The 
# fourth account should not receive user input and should retain the default 
# values set by the constructor. Then, define another function named 
# show_values() that accepts a BankAccount object, displays its details, calls the 
# method to deduct the monthly fee, and then displays the updated balance. This 
# function should also call the static method that explains the account policy. 

class BankAccount:
    def __init__(self, account_number="", owner_name="", balance=0.0):
        self._account_number = account_number
        self._owner_name = owner_name
        self._balance = balance

    # Getters and Setters
    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        self._account_number = value

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        self._owner_name = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    # Deduct monthly fee
    def deduct_monthly_fee(self):
        self._balance -= 4.00

    # Static method
    @staticmethod
    def explain_account_policy():
        print("A $4.00 service fee will be deducted from your account every month.")


# Function to get user input and return a BankAccount object
def get_data():
    account_number = input("Enter account number: ")
    owner_name = input("Enter owner name: ")
    balance = float(input("Enter balance: "))
    return BankAccount(account_number, owner_name, balance)


# Function to display details and update balance
def show_values(account):
    print("\nAccount Details")
    print("Account Number:", account.account_number)
    print("Owner Name:", account.owner_name)
    print("Balance before fee:", account.balance)

    account.deduct_monthly_fee()

    print("Balance after fee:", account.balance)

    # Call static method
    BankAccount.explain_account_policy()


# Main program
print("Enter details for Account 1")
acc1 = get_data()

print("\nEnter details for Account 2")
acc2 = get_data()

print("\nEnter details for Account 3")
acc3 = get_data()

# Fourth account with default values
acc4 = BankAccount()

# Display all accounts
show_values(acc1)
show_values(acc2)
show_values(acc3)
show_values(acc4)