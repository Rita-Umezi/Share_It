"""
A university stores student course registration
write a program that:
stores two course records using tuples
stores registered students for each course in a list
stores students who passed prerequisite courses in a set
finds students eligible to take the course using set intersection
stores course and eligible students in a dictionary
"""

# Course records as tuples (course_code, course_name)
course1 = ("CS101", "Introduction to Computer Science")
course2 = ("CS102", "Data Structures")

# Registered students lists for each course
registered_cs101 = ["Alice", "Bob", "Charlie", "Dana"]
registered_cs102 = ["Bob", "Eve", "Frank", "Charlie"]

# Students who passed prerequisite courses
passed_prereqs = {"Alice", "Charlie", "Frank", "George"}

# Determine eligible students for each course
eligible_cs101 = set(registered_cs101) & passed_prereqs
eligible_cs102 = set(registered_cs102) & passed_prereqs

# Store the results in a dictionary mapping course code to eligible students
eligible_dict = {
    course1[0]: eligible_cs101,
    course2[0]: eligible_cs102
}

# Display results
print(f"Eligible students for {course1[0]} ({course1[1]}): {eligible_cs101}")
print(f"Eligible students for {course2[0]} ({course2[1]}): {eligible_cs102}")
print("\nDictionary of eligible students:")
for course, students in eligible_dict.items():
    print(f"{course}: {students}")

