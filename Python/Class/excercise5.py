"""
Create function with default parameter:
calculate_salary(basic, allowance = 20000)
"""
def calculate_salary(basic, allowance = 20000):
    return basic + allowance
basic_salary = int(input("Enter your basic Salary: "))

print("Your Total take home is: ", calculate_salary(basic_salary))


"""" Write recursive function: Sum of numbers from 1 to n
"""
def sum_of_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_numbers(n-1)
n = int(input("Enter a number: "))
print("The sum of numbers from 1 to", n, "is:", sum_of_numbers(n))