# write an if statement to check if the color is green, print("5 poinrts is earned"). write a passed and failed version

# alien_color="red"
# if alien_color=="green":
#      print("You have earned 5 points")
# elif alien_color=="yellow":
#      print("Nothing for you")
# else:
#      print("Sorry")

""" order(highest to lowest)
**
*,/,//,%,
+,-
comparism
not
and
or
assignemnt

identity, bitwise,membership operators(read about it)
"""

"""
Create a list of 5 numbers, use loop to print each number, print the square of each number
"""
# numbers=[1,2,3,4,5]
# for num in numbers:
#      print(num)
     
# squares=[x**2 for x in numbers]    
# print(squares)

# total=0
# for num in numbers:
#      total+=num

# print(total)

"""
creeate a list of numbers from 1-20, use loop to count how many are even and how many are odd, print both results
"""

# my_numbers=list(range(1,21))
# evenCount=0
# oddCount=0

# for num in my_numbers:
#      if num%2==0:
#           evenCount+=1
#      else: oddCount+=1  

# print(evenCount)   
# print(oddCount)   
          
                   
"""
write a function that accepts a list of numbers, 
the function should return the total and average
call the function using a sample list
modify it to return the highest value as well
"""          


def analyze_numbers(numbers):
    total = 0
    highest = numbers[0]  

    for num in numbers:
        total += num        
             
        if num > highest:   
            highest = num

    average = total / len(numbers)
    return total, average, highest

numbers = [1, 2, 3, 4, 5]
print(analyze_numbers(numbers))

