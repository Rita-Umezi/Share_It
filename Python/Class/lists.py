#list lecture, also learnt constructor
numbers=list(range(0,11))#constructor example
mixed_variables=["Grace", 100, 7.5, "Joy", True]
student=["Rita", "Chisom", "Rebecca", "Ola", "Michael"]
student[1]="Ayrra"

# for s in student:
#     print(s)

student.insert(6, "Chris")
print(student)
#append adds a new item to the end of the list
#insert adds a new item at the specified index
#to use remove(), you have to add the specific value you want to remove eg student.remove("rita")
#to use pop(), you have to add the index of what you want to remove eg student.pop(4)
#.count() finds the number of the list i think
#.sort() helps to arrange the list in ascending order
#slicing list function removes a portion of the code, syntax:list[start:end:step] eg student[1:3]
student.remove("Ayrra")
# student.pop(2)
# student.reverse()
print(student[0:3])

#list comprehension(shortcut for lists) below
myList=[1,2,3,4,5]
squares=[x**2 for x in myList]
print(squares)

#another example of list comprehension
range_squares=[x**2 for x in range(6)]
print(range_squares)
odd=[x for x in range_squares if x%2 !=0]
print(odd)

"""
Excercise: create a program that stores student names and scores using lists and allows:
Adding new students & scores
Finding the highest/lowest score
Calculating the average score
"""
students=["Rita", "Chisom", "Rebecca", "Ola", "Michael"]
scores=[45, 78, 90, 56, 67]

students.append(" Rita")
scores.append(45)
print("The scores of students are ", scores)
print("The students are ", students)

max_score=max(scores)
print("Max score= ", max_score)
lowest_score=min(scores)
print("Lowest score= ", lowest_score)

average=sum(scores)/len(scores)
print("Average score= ", average)




