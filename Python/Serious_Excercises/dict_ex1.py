"""
write a python program that uses a dictionary to store student names as keys and their scores as values
create a dictionary containing 5 student and their scores
display all student names and their scores 
find the student with the highest score
calculate the average of the scores
"""

scores={
    "Rita":23,
    "Ritz":234,
    "Ritolo":23,
    "RitQ":21,
    "Ritzuzzy":25
}
print(scores)#display all student names and their scores 
highest_score_student = max(scores, key=scores.get)
highest_score = max(scores.values())
print(f"\nThe student with the highest score is {highest_score_student} with a score of {highest_score}.")


#  Calculate the average of the scores
average_score = sum(scores.values()) / len(scores)
print(f"The average score of all students is {average_score:.2f}.")





