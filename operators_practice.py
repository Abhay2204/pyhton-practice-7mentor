"""
Python Operators Practice Questions
----------------------------------
This file contains practice questions covering all Python operator categories:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators
8. Operator Precedence & Challenges
"""

# ==========================================
# 1. ARITHMETIC OPERATORS
# ==========================================

a = 23
b = 5

print("Addition (a + b)      :", a + b)
print("Subtraction (a - b)   :", a - b)
print("Multiplication (a * b):", a * b)
print("Division (a / b)      :", a / b)
print("Floor Division (a // b):", a // b)
print("Modulus (a % b)       :", a % b)
print("Exponentiation (a ** b):", a ** b)


# ==========================================
# 2. ASSIGNMENT OPERATORS
# ==========================================

count = 10

count += 5
print("After += 5 :", count)
count -= 3
print("After -= 3 :", count)
count *= 2
print("After *= 2 :", count)
count //= 4
print("After //= 4:", count)
count %= 5
print("After %= 5 :", count)


# ==========================================
# 3. COMPARISON OPERATORS
# ==========================================

x = 15
y = 20
z = 15

print("x == z:", x == z)
print("x != y:", x != y)
print("x > y :", x > y)
print("x < y :", x < y)
print("x >= z:", x >= z)
print("y <= x:", y <= x)
print("10 <= x <= 20:", 10 <= x <= 20)


# ==========================================
# 4. LOGICAL OPERATORS
# ==========================================

has_license = True
has_insurance = False
age = 22

can_drive = (age >= 18) and has_license and has_insurance
can_rent = has_license or has_insurance
is_minor = not (age >= 18)
print("Can Drive (and) :", can_drive)
print("Can Rent (or)   :", can_rent)
print("Is Minor (not)  :", is_minor)


# ==========================================
# 5. IDENTITY OPERATORS
# ==========================================

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 == list2 (Same values?) :", list1 == list2)
print("list1 is list2 (Same memory?)  :", list1 is list2)
print("list1 is list3 (Same memory?)  :", list1 is list3)
print("list1 is not list2             :", list1 is not list2)


# ==========================================
# 6. MEMBERSHIP OPERATORS
# ==========================================

text = "Python Programming at 7Mentor"
skills = ["Python", "Java", "SQL"]
student_data = {"name": "Abhay", "role": "Student"}

print("'Python' in text        :", "Python" in text)
print("'C++' not in text       :", "C++" not in text)
print("'Java' in skills        :", "Java" in skills)
print("'name' in student_data  :", "name" in student_data)
print("'Student' in student_data.values():", "Student" in student_data.values())


# ==========================================
# 7. BITWISE OPERATORS
# ==========================================

m = 12  # Binary: 1100
n = 5   # Binary: 0101

print("Bitwise AND (m & n) :", m & n)
print("Bitwise OR  (m | n) :", m | n)
print("Bitwise XOR (m ^ n) :", m ^ n)
print("Bitwise NOT (~m)    :", ~m)
print("Left Shift  (m << 2):", m << 2)
print("Right Shift (m >> 2):", m >> 2)


# ==========================================
# 8. OPERATOR PRECEDENCE & MINI CHALLENGES
# ==========================================

result = 10 + 2 * 3 ** 2 - 8 // 4
print("10 + 2 * 3 ** 2 - 8 // 4 =", result)

price = 100
qty = 3
subtotal = price * qty
discount = (subtotal * 0.10) if subtotal > 200 else 0
after_discount = subtotal - discount
shipping = 0 if after_discount >= 250 else 15
final_payable = after_discount + shipping
print("Subtotal     :", subtotal)
print("Discount     :", discount)
print("Shipping     :", shipping)
print("Final Payable:", final_payable)
