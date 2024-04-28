# 1. Python List Transformation
# Task 1: Given the list of grades:
print("task 1 output:")
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse = True)
print(grades)

# Task 2 Calculate the average grade and display it.
print("task 2 output:")
a = sum(grades) / float(len(grades))
print(a , " is the average")

# task 3 Replace any grade below 80 with the value Failed

print("task 3 output:")
pass_failed = ['pass' if grade >= 80 else 'failed' for grade in grades]
print(pass_failed)