# task 1 Find out which students both 
# submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

a="Alice"
b="Bob"
c="Charlie"
d="David"
e="Eve"
f="Frank"

print("Task 1 output:")
if a in submitted and a in attended:
    print(a," submitted and attended")
else:
    print(a, " did not do both")

if b in submitted and b in attended:
    print(b," submitted and attended")
else:
    print(b, " did not do both")

if c in submitted and c in attended:
    print(c," submitted and attended")
else:
    print(c, " did not do both")

if d in submitted and d in attended:
    print(d," submitted and attended")
else:
    print(d, " did not do both")

if e in submitted and e in attended:
    print(e," submitted and attended")
else:
    print(e, " did not do both")

if f in submitted and f in attended:
    print(f," submitted and attended")
else:
    print(f, " did not do both")


# Task 2: Check if the two lists are identical in 
# terms of their content, regardless of order.
print("Task 2 output:")
if submitted == attended:
    print("The list are identical")
else:
    print("The lists are not identical")

# Task 3: Using list methods, remove any 
# student from the attended list who did 
# not submit their assignment.

print("Task 3 output:")
attended.remove("Eve")
attended.remove("Frank")
print(attended)





