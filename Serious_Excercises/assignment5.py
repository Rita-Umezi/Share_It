# Create a class called Course with:

# Instance variables: course_code, student_count

# Class variable: max_students = 50

# Tasks:

# Create 2 course objects

# Write a setter to update student count

# Ensure student count does not exceed max_students

# Write a getter to display course details

class Course:
    max_students = 50  # Class variable shared by all instances

    def __init__(self, course_code, student_count):
        self.course_code = course_code  # Instance variable for the course code
        self._student_count = student_count  # Instance variable for the student count (protected)

    @property
    def student_count(self):
        return self._student_count  # Getter method to retrieve the student count

    @student_count.setter
    def student_count(self, value):
        if value <= Course.max_students:  # Validate that the student count does not exceed max_students
            self._student_count = value  # Setter method to update the student count
        else:
            print(f"Student count cannot exceed {Course.max_students}.")
# Create 2 course objects
course1 = Course("CS101", 30)
course2 = Course("MATH201", 45)
# Display course details
courses = [course1, course2]
for course in courses:
    print(f"Course Code: {course.course_code}, Student Count: {course.student_count}, Max Students: {Course.max_students}")
# Update student count for course1
course1.student_count = 40  # Valid update
print(f"Course: {course1.course_code}, Updated Student Count: {course1.student_count}, Max Students: {Course.max_students}")