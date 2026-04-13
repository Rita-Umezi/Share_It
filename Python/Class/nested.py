    #print a particular element in a list using while loop and conditional statements
my_list = [10, 20, 30, 40, 50, 60]
index = 0
target = 40

while index < len(my_list):
    if my_list[index] == target:
        print(f"Found {target} at index {index}")
        break
    index += 1
else:
    print(f"{target} not found in the list")
    
     #Nested loop
for i in range(1,16):
     for j in range(1, i+1):
         print("*", end=" ")
     print()  # gives a triangle-like look
     
#write a program that prints numbers from 1 to 10 using a for loop 
#print:even numbers only and odd numbers only     
print("Even numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:
        print(num, end=" ")

print("\nOdd numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 != 0:
        print(num, end=" ")
        

#question to get and display the vowels and consonants in a word
word=input("Enter a word")

word= word.lower()
vowels="aeiou"
vowelCount=0           
consonantCount=0
for char in word:
    if char in vowels:
        vowelCount += 1
    elif char.isalpha():  # Check if the character is a consonant (i.e., an alphabet that is not a vowel)
        consonantCount += 1           
print(f"Vowels: {vowelCount}")
print(f"Consonants: {consonantCount}")