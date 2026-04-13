"""
write a program that stores a 3x3 matrix in a list and then prints the sum of each row
"""
matrix=[]
for i in range(3):
    row=[]
    for j in range(3):
        content=int(input(f"Enter element for row {i+1}, column {j+1}: "))
        row.append(content)
    matrix.append(row)
print(matrix)

for row in matrix:
    row_sum=sum(row)
    print(f"Sum of row {matrix.index(row)+1}: {row_sum}")