# Write a function to check: even or odd number
def checker(a):
    if a % 2 == 0:
        print(a, "is an even number")
    else:
        print(a, "is an odd number")

number = int(input("Enter any number: "))

checker(number)

""""Create a student grade function
A >=70, B >=60, C >=50, D >=45, F <45"""

def grade(score):
    if score >=70:
        print("Your score is A")
    elif score >= 60:
        print("Your score is B")
    elif score >= 50:
        print("Your score is C")
    elif score >= 45:
        print("Your score is D")
    elif score < 45:
        print("Your score is F")
    else:
        print("Invalid Score")
        
user_score = int(input("Enter your Score: "))

grade(user_score)