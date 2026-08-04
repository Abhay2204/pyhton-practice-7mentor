"""
Python Control Flow Practice Questions
---------------------------------------
This file contains practice questions covering decision making (if/elif/else),
loops (for, while), loop control statements (break, continue, pass), and range().
"""

# ==========================================
# 1. CONDITIONAL STATEMENTS (IF / ELIF / ELSE)
# ==========================================

marks = 85

if marks >= 90:
    grade = 'A'
elif marks >= 80:
    grade = 'B'
elif marks >= 70:
    grade = 'C'
else:
    grade = 'F'

print(f"Marks: {marks} -> Grade: {grade}")

# Leap year check
year = 2024

import calendar
print(f"Approach 1 (calendar.isleap): {year} is leap year? -> {calendar.isleap(year)}")

if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False
print(f"Approach 2 (Step-by-Step): {year} is leap year? -> {is_leap}")

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Approach 3 (Combined Condition): {year} is a Leap Year.")


# ==========================================
# 2. TERNARY OPERATOR
# ==========================================

num = 14
result = "Even" if num % 2 == 0 else "Odd"
print(f"Number {num} is {result}")


# ==========================================
# 3. FOR LOOPS & RANGE()
# ==========================================

print("Numbers 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

even_sum = 0
for i in range(2, 21, 2):
    even_sum += i
print("Sum of even numbers 1 to 20:", even_sum)

print("Countdown 10 to 1:")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")


# ==========================================
# 4. WHILE LOOPS
# ==========================================

n = 5
factorial = 1
temp = n

while temp > 0:
    factorial *= temp
    temp -= 1

print(f"Factorial of {n} is: {factorial}")


# ==========================================
# 5. LOOP CONTROL STATEMENTS
# ==========================================

print("Numbers 1-10 skipping multiples of 3:")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

items = [12, 45, 67, 89, 23, 90]
target = 89
found = False

for item in items:
    if item == target:
        found = True
        break

print(f"Target {target} found in list:", found)


# ==========================================
# 6. FOR-ELSE LOOPS
# ==========================================

number = 17
is_prime = True

if number < 2:
    is_prime = False
else:
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    else:
        print(f"{number} is a PRIME number (confirmed by for-else).")
