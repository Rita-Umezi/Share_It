# Write a Python program that declares variables to store an hourly wage and the 
# number of hours worked. Prompt the user to enter values for the hourly rate and 
# the number of hours worked. Create a function that accepts these two values as 
# parameters and calculates the gross weekly pay. The gross pay should be 
# computed as follows: for the first 50 hours, multiply the number of hours worked 
# by the hourly rate; for any hours worked beyond 50, calculate the extra hours at 
# 2.5 times the hourly rate and add this to the regular pay. 
# After computing the gross pay, calculate the net pay by subtracting withholding 
# tax. The withholding tax should be determined based on the gross pay as follows: 
# if the gross pay is greater than 10,000, the tax is 25% of the gross pay; if the 
# gross pay is greater than 6,000 but not more than 10,000, the tax is 20% of the 
# gross pay; otherwise, the tax is 10% of the gross pay. Finally, display both the 
# gross pay and the net pay.

# Function to calculate gross pay
def calculate_gross_pay(hourly_rate, hours_worked):
    if hours_worked <= 50:
        gross_pay = hours_worked * hourly_rate
    else:
        regular_pay = 50 * hourly_rate
        extra_hours = hours_worked - 50
        overtime_pay = extra_hours * (2.5 * hourly_rate)
        gross_pay = regular_pay + overtime_pay
    return gross_pay


# Function to calculate net pay after tax
def calculate_net_pay(gross_pay):
    if gross_pay > 10000:
        tax = 0.25 * gross_pay
    elif gross_pay > 6000:
        tax = 0.20 * gross_pay
    else:
        tax = 0.10 * gross_pay
    
    net_pay = gross_pay - tax
    return net_pay


# Main program
hourly_rate = float(input("Enter hourly rate: "))
hours_worked = float(input("Enter number of hours worked: "))

gross_pay = calculate_gross_pay(hourly_rate, hours_worked)
net_pay = calculate_net_pay(gross_pay)

print(f"Gross Pay: {gross_pay}")
print(f"Net Pay: {net_pay}")