#  Create a class called Student with the following:

# Instance variables: name, score

# Class variable: school_name (same for all students)

# Create at least 3 student objects

# Display each student’s name, score, and school name

# Use a getter method to retrieve the score

# Use a setter method to update the score 

class Student:
    school_name = "Greenwood High School"  # Class variable shared by all instances

    def __init__(self, name, score):
        self.name = name  # Instance variable for the student's name
        self._score = score  # Instance variable for the student's score (protected)

    @property
    def score(self):
        return self._score  # Getter method to retrieve the score

    @score.setter
    def score(self, value):
        if 0 <= value <= 100:  # Validate that the score is between 0 and 100
            self._score = value  # Setter method to update the score
        else:
            print("Score must be between 0 and 100.")
# Create at least 3 student objects
student1 = Student("Alice", 85)
student2 = Student("Bob", 92)
student3 = Student("Charlie", 78)

# Display each student’s name, score, and school name
students = [student1, student2, student3]
for student in students:
    print(f"Name: {student.name}, Score: {student.score}, School: {Student.school_name}")