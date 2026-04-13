"""" print keyword displays a value while return sends value back and stops execution
recursion: function calling itself. base case; stops recursion and recursive case;
"""

#recursive function that gets the factorial of any number

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(3))

#recursive function of fibonnacci series
def fibonacci(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n=int(input("Enter the number of terms: "))    
for i in range(n):
    print(fibonacci(i), end=" ")
    
#example of default parameter
def multiply (b, a= 20):
    print (a * b)
        
multiply(30)