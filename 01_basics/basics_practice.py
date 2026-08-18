"""
Python Basics Practice Questions
---------------------------------
This file contains basic practice questions covering variables, data types,
type casting, input/output formatting, arithmetic, comparison, logical,
assignment operators, bitwise, base conversions, string methods, list, and tuple operations.
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
# 3. INPUT / OUTPUT & USER INPUT
# ==========================================

# Q6: Format and print a multi-line output using f-strings.
product = "Laptop"
price = 899.99
quantity = 2
total = price * quantity

print(f"Product: {product}\nPrice: ${price}\nQuantity: {quantity}\nTotal Cost: ${total:.2f}")

# Q7: Example of getting user input (commented out so file runs automatically)
# user_name = input("Enter your name: ")
# user_age = int(input("Enter your age: "))
# print(f"Hello {user_name}, next year you will be {user_age + 1} years old.")


# ==========================================
# 4. ARITHMETIC OPERATORS
# ==========================================

a = 17
b = 5

# Q8: Perform addition, subtraction, multiplication, division, floor division, modulus, and exponentiation.
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

# Q9: Check comparison operations.
print("x == z:", x == z)
print("x != y:", x != y)
print("x > y:", x > y)
print("x <= z:", x <= z)

# Q10: Evaluate logical expressions using 'and', 'or', 'not'.
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

# Q11: Use shorthand assignment operators (+=, -=, *=, /=).
count += 5  # count = 15
count *= 2  # count = 30
count -= 4  # count = 26
count //= 3 # count = 8

print("Final count value:", count)

print("=" * 60)


# ==========================================
# 7. OPERATORS & MEMORY
# ==========================================

# Identity vs Equality: is vs ==
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print("list1 == list2 (Value check):", list1 == list2)
print("list1 is list2 (Memory check id):", list1 is list2)

# Membership Operators: in, not in
fruits = ["apple", "banana", "cherry"]
print("'banana' in fruits:", "banana" in fruits)
print("'mango' not in fruits:", "mango" not in fruits)

# Chained Comparisons: 10 <= x <= 20
num_check = 15
print("10 <= num_check <= 20:", 10 <= num_check <= 20)

# Bitwise Operators: &, |, ^, ~, <<, >>
p, q = 6, 3
print("Bitwise AND (6 & 3):", p & q)
print("Bitwise OR (6 | 3):", p | q)
print("Bitwise XOR (6 ^ 3):", p ^ q)
print("Bitwise NOT (~6):", ~p)
print("Left Shift (6 << 1):", p << 1)
print("Right Shift (6 >> 1):", p >> 1)

print("=" * 60)


# ==========================================
# 8. BASE & ASCII CONVERSIONS
# ==========================================

# Base Conversions: bin(), oct(), hex(), int("1010", 2)
num_val = 10
print("bin(10):", bin(num_val))
print("oct(10):", oct(num_val))
print("hex(10):", hex(num_val))
print("int('1010', 2):", int("1010", 2))

# ASCII Conversions: ord('A'), chr(65)
print("ord('A'):", ord('A'))
print("chr(65):", chr(65))

print("=" * 60)


# ==========================================
# 9. STRING METHODS & SLICING
# ==========================================

msg = "PythonProgramming"
print("Slicing [0:6]:", msg[0:6])
print("Reversed string msg[::-1]:", msg[::-1])

raw_text = "   hello python   "
print("strip():", f"'{raw_text.strip()}'")

words = msg.split("n")
print("split('n'):", words)

print("replace('Python', 'Java'):", msg.replace("Python", "Java"))
print("'12345'.isdigit():", '12345'.isdigit())
print("'Python'.isalpha():", 'Python'.isalpha())

print("=" * 60)


# ==========================================
# 10. LIST OPERATIONS
# ==========================================

nums = [10, 20]
nums.append(30)
nums.extend([40, 50])
nums.insert(1, 15)
print("List After Adding:", nums)

nums.pop(0)
nums.remove(40)
print("List After Removing:", nums)

sample_list = [5, 2, 9, 1]
sample_list.sort(reverse=True)
print("List Sorted Descending:", sample_list)

print("=" * 60)


# ==========================================
# 11. TUPLE OPERATIONS
# ==========================================

t_single = (5,)
print("Single element tuple:", type(t_single), t_single)

a_val, b_val, *c_val = (1, 2, 3, 4, 5)
print("Tuple Unpacking -> a:", a_val, "| b:", b_val, "| *c:", c_val)
