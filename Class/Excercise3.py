"""
simulate a login system where user is prompted to enter username and password.
INSTRUCTIONS
Store a correct username and password in variables
Prompt the user to enter their username and password
Compare the entered credentials with the stored ones
If both match, print a success message                 
If both match, print a success message
If either the username or password is incorrect, print a failure message
"""

correctUsername="Rita"
correctPAssword="qwerty"

username=input("Enter your username: ")
password=input("Enter your password: ")

if username==correctUsername and password==correctPAssword:
    print("Login successful")
else:
    print("Login failed")
    

"""
write a program that classifies a student's score
INSTRUCTIONS
Ask a user to enter a score
Convert the score to an integer
Use condition to assign the grades; A for 70-100, B for 60-69, C for 50-59, D for 40-49, F for below 40
"""    

score=input("Enter your score: ")
score=int(score)

if score>=70 and score<=100:
    print("A")
elif score>=60 and score<=69:
    print("B")
elif score>=50 and score<=59:
    print("C")
elif score>=40 and score<=49:
    print("D")
else:
    print("F")
    
    
"""
Determine if a student is eligible for a scholarship
RULES
Score must be 70 or above
Age must be 18 or below
Print: 'Eligible for scholarship' if both conditions are met
Print: 'Not eligible for scholarship' if any condition is not met
"""

score=input("Enter your score: ")
score=int(score)
age=input("Enter your age: ")
age=int(age)

if score>=70 and age<=18:
    print("Eligible for scholarship")
else:
    print("Not eligible for scholarship")