# ==========================================
# 1. COUNT() METHOD
# count() counts how many times an element appears in a list
# ==========================================

number = [20, 33, 50, 43, 12, 50, 50, 50]
print(number.count(50))


# ==========================================
# 2. INDEX() METHOD
# index() returns the position of an element in a list
# ==========================================

name = ["suruchi", "kanika", "riya", "radha"]
print(name.index("riya"))


# ==========================================
# 3. POP() METHOD
# pop() removes an element using its index number
# ==========================================

number = [20, 45, 40, 20]
number.pop(0)
print(number)


# ==========================================
# 4. SORT() METHOD
# sort() arranges list elements in ascending order
# ==========================================

student_name = ["suruchi", "kanika", "riya", "radha"]
student_name.sort()
print(student_name)


# ==========================================
# 5. SORT(REVERSE=TRUE) METHOD
# reverse=True arranges list elements in descending order
# ==========================================

student_name = ["suruchi", "kanika", "riya", "radha"]
student_name.sort(reverse=True)
print(student_name)


# ==========================================
# 6. REMOVE() METHOD
# remove() removes a specific value from a list
# ==========================================

name = ["suruchi", "kanika", "riya", "radha"]
name.remove("riya")
print(name)


# ==========================================
# 7. APPEND() METHOD
# append() adds a new element at the end of a list
# ==========================================

number = [22, 25, 40, 50]
number.append(50)
print(number)


# ==========================================
# 8. TYPE CONVERSION
# Type conversion changes one data type into another
# ==========================================

a = 40

# Convert integer into boolean
a = bool(a)
print(type(a))

# Convert boolean into float
a = float(a)
print(type(a))

# Convert float into string
a = str(a)
print(type(a))


# ==========================================
# 9. COMPLEX DATA TYPE
# Complex numbers contain real and imaginary parts
# ==========================================

x = 2 + 3j
print(type(x))


# ==========================================
# 10. TAKING INPUT FROM USER
# input() takes information from the user
# ==========================================

# Taking name as input
name = input("Enter your name: ")

# Taking age as integer input
age = int(input("Enter your age: "))

# Taking salary as float input
salary = float(input("Enter your salary: "))

# Taking student status as input
is_student = input("Are you a student? (True/False): ")


# ==========================================
# 11. PRINTING VALUES AND DATA TYPES
# type() tells us the data type of a variable
# ==========================================

print("Name:", name)
print("Data Type:", type(name))

print("Age:", age)
print("Data Type:", type(age))

print("Salary:", salary)
print("Data Type:", type(salary))

print("Student:", is_student)
print("Data Type:", type(is_student))


# ==========================================
# 12. TUPLE DATA TYPE
# Tuple stores multiple values inside round brackets
# Tuple is immutable (cannot be changed)
# ==========================================

student_name = ("suruchi", "kriti", "neha")
print(type(student_name))