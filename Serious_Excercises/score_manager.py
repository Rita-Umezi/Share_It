"""
student score manager design a program that allows a user to enter students'scores into a list and then displays
the highest score, lowest score and average score.
"""
scores=[]
score=int(input("Enter number of  scores: "))
for i in range(score):
    input_score=int(input("Enter score: "))
    scores.append(input_score)
print("Highest score: ", max(scores))
print("Lowest score: ", min(scores))
print("Average score: ", sum(scores)/len(scores))


