number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))


print("The sum is: ", number1 + number2)
print("The difference is: ", number1 - number2)
print("The product is: ", number1 * number2)
print("The quotient is: ", number1 / number2)

# #this code is for another question
monthlyAllowance=input("Enter your monthly allowance: ")
transportCost=input("Enter your daily transport cost: ")
feedingCost=input("Enter your daily feeding cost: ")

monthlyAllowance = int(monthlyAllowance)
transportCost = int(transportCost)
feedingCost = int(feedingCost)

totalSpent= transportCost + feedingCost

monthlyAllowance - totalSpent #remaining allowance after daily expenses


#another questions
unit=input("Enter the number of units consumed: ")
unit = int(unit)
costPerUnit=input("Enter the cost per unit: ")
costPerUnit = int(costPerUnit)
totalCost=unit*costPerUnit
print("The total cost is: ", totalCost)

#get 5% VAT
VAT=totalCost*0.05
print("The VAT is: ", VAT)
#final payable amount
payableAmount=totalCost+VAT
print("The payable amount is: ", payableAmount)

#clear bill summary
print("Bill Summary")
print("Units Consumed: ", unit)
print("Cost Per Unit: ", costPerUnit)
print("Total Cost: ", totalCost)
print("VAT: ", VAT)
print("Payable Amount: ", payableAmount)
remainingAllowance=monthlyAllowance-(totalCost*30)
print("Your remaining allowance after daily expenses is: ", remainingAllowance)

