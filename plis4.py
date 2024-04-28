# Task 1: Given the lists:
# Filter out students who have grades below 80. 
# Print the name, grade and activiy. 
# Expected Outcome "Jane", 78, "Art"

students = ["John", "Doe", "Jane", "Smith"]
grades = [85, 90, 78, 88]
activities = ["Football", "Music", "Art", "Dance"]

filtered_grades = [g for g in grades if g < 80]
print(students [2], filtered_grades, activities [2])

# Task 2: For the remaining students, add students 
# name in a new list named students_approved. 
# Expected Outcome: 
# students_approved = ["John", "Doe", "Smith"]

students_approved = []
students_approved.append("John")
students_approved.append("Doe")
students_approved.append("Smith")

# Task 3: Print the list students_approved

print(students_approved)