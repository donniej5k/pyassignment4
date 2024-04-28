# Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print("task 1 results")
print(temperatures[7:14])

# Task 2: Extract all the temperatures above 100.

t2 = [t for t in temperatures if t >= 100]
print("task 2 results")
print(t2)

# Task 3: Reverse the list and extract temperatures 
# from the 5th to the 10th day of the reversed list.

def Reverse(temperatures):
    t3 = temperatures[::-1]
    return t3
print("task 3 results")
tr = (Reverse(temperatures))

print(tr[4:9])
