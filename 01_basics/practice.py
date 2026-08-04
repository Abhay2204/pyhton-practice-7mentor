"""
Python Basics Practice Questions
---------------------------------
This file contains basic practice questions covering variables, data types,
type casting, input/output formatting, arithmetic, comparison, and logical operators.
"""

# ==========================================
# 1. VARIABLES & DATA TYPES
# ==========================================

# Q1: Declare variables for age (integer), height (float), name (string), and is_student (boolean).
age = 20
height = 5.9
name = "Alice"
is_student = True

# Q2: Print each variable along with its data type using type().
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Is Student:", is_student, "| Type:", type(is_student))


# ==========================================
# 2. TYPE CASTING
# ==========================================

# Q3: Convert string "100" to an integer and add 50 to it.
num_str = "100"
num_int = int(num_str) + 50
print("Converted string to int + 50:", num_int)

# Q4: Convert float 12.87 to an integer (truncates decimal part).
val_float = 12.87
val_int = int(val_float)
print("Float 12.87 as int:", val_int)

# Q5: Convert integer 0 and integer 42 to boolean values using bool().
print("bool(0):", bool(0))
print("bool(42):", bool(42))


# ==========================================
# 3. INPUT / OUTPUT & F-STRINGS
# ==========================================

# Q6: Format and print a multi-line output using f-strings.
product = "Laptop"
price = 899.99
quantity = 2
total = price * quantity

print(f"Product: {product}\nPrice: ${price}\nQuantity: {quantity}\nTotal Cost: ${total:.2f}")


# ==========================================
# 4. ARITHMETIC OPERATORS
# ==========================================

a = 17
b = 5

# Q7: Perform addition, subtraction, multiplication, division, floor division, modulus, and exponentiation.
print("Addition (17 + 5):", a + b)
print("Subtraction (17 - 5):", a - b)
print("Multiplication (17 * 5):", a * b)
print("Division (17 / 5):", a / b)
print("Floor Division (17 // 5):", a // b)
print("Modulus (17 % 5):", a % b)
print("Exponentiation (17 ** 2):", a ** 2)


# ==========================================
# 5. COMPARISON & LOGICAL OPERATORS
# ==========================================

x = 15
y = 20
z = 15

# Q8: Check comparison operations.
print("x == z:", x == z)
print("x != y:", x != y)
print("x > y:", x > y)
print("x <= z:", x <= z)

# Q9: Evaluate logical expressions using 'and', 'or', 'not'.
has_license = True
has_car = False

can_drive = has_license and has_car
can_travel = has_license or has_car
cannot_drive = not has_license

print("Can drive (and):", can_drive)
print("Can travel (or):", can_travel)
print("Not has license:", cannot_drive)


# ==========================================
# 6. ASSIGNMENT OPERATORS
# ==========================================

count = 10

# Q10: Use shorthand assignment operators (+=, -=, *=, /=).
count += 5  # count = 15
count *= 2  # count = 30
count -= 4  # count = 26
count //= 3 # count = 8

print("Final count value:", count)

# ==========================================
# 7. STRING CONCATENATION EXERCISE
# ==========================================
first_name = "ANNURUDH"
last_name = "JADAV"
full_name = first_name + " " + last_name
print("Full Name Concatenation:", full_name)
