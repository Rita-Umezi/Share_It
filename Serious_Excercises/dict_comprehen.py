# you are given a list of recored representing employee, where each record is a tuple in the form: (name, department, salary)

# a. write a python program using dictionary comprehensin to create a dictionary that maps each department to the highest salary within that department
# b. explain why dictionary comprehension is preferable to a traditional loop in this case


employees = [
    ("Alice", "Engineering", 85000),
    ("Bob", "Engineering", 92000),
    ("Charlie", "Engineering", 78000),
    ("David", "Sales", 65000),
    ("Eve", "Sales", 72000),
    ("Frank", "HR", 55000),
]

# Get unique departments using descriptive variable names
departments = {department for employee_name, department, salary in employees}

# Dictionary comprehension to get the highest salary per department
max_salary_by_dept = {
    department: max(salary for employee_name, dept, salary in employees if dept == department)
    for department in departments
}

print(max_salary_by_dept)

# b. Why dictionary comprehension is preferable

# Dictionary comprehension is often better than a traditional loop in this case because:

# More concise:
# It allows you to write the logic in a single, compact expression instead of multiple lines with loops and conditionals.
# Better readability (once understood):
# The intent is clear: “for each department, assign the maximum salary.” A traditional loop would require initializing the dictionary and updating it step by step.
# Less boilerplate code:
# No need to manually check if a key exists or update values repeatedly.
# Pythonic style:
# It follows Python’s emphasis on clean and expressive code.