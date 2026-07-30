"""
Python Control Flow Practice Questions
---------------------------------------
This file contains practice questions covering decision making (if/elif/else),
loops (for, while), loop control statements (break, continue, pass), and range().

Try solving each question or run this file to verify the solutions.
"""

# ==========================================
# 1. CONDITIONAL STATEMENTS (IF / ELIF / ELSE)
# ==========================================

# Q1: Write an if-elif-else block to assign grades based on marks:
# 90 or above -> 'A', 80-89 -> 'B', 70-79 -> 'C', below 70 -> 'F'.
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

# Q2: Check if a given year is a leap year (3 Different Approaches)
year = 2024

# Approach 1: Python's built-in 'calendar' module (Simplest 1-Liner)
import calendar
print(f"Approach 1 (calendar.isleap): {year} is leap year? -> {calendar.isleap(year)}")

# Approach 2: Step-by-Step logic (Easiest to read & understand)
if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False
print(f"Approach 2 (Step-by-Step): {year} is leap year? -> {is_leap}")

# Approach 3: Standard single-line conditional formula
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Approach 3 (Combined Condition): {year} is a Leap Year.")




# ==========================================
# 2. TERNARY OPERATOR (CONDITIONAL EXPRESSION)
# ==========================================

# Q3: Use a single-line ternary operator to check if a number is Even or Odd.
num = 14
result = "Even" if num % 2 == 0 else "Odd"
print(f"Number {num} is {result}")


# ==========================================
# 3. FOR LOOPS & RANGE()
# ==========================================

# Q4: Print numbers from 1 to 5 using for loop and range().
print("Numbers 1 to 5:")
for i in range(1, 6):
    print(i, end=" ")
print()

# Q5: Calculate the sum of even numbers between 1 and 20 (inclusive).
even_sum = 0
for i in range(2, 21, 2):
    even_sum += i
print("Sum of even numbers 1 to 20:", even_sum)

# Q6: Print numbers in reverse from 10 down to 1.
print("Countdown 10 to 1:")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# Q7: Iterate through a list of items using enumerate() to print index and value.
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")


# ==========================================
# 4. WHILE LOOPS
# ==========================================

# Q8: Calculate the factorial of a number (5!) using a while loop.
n = 5
factorial = 1
temp = n

while temp > 0:
    factorial *= temp
    temp -= 1

print(f"Factorial of {n} is: {factorial}")


# ==========================================
# 5. LOOP CONTROL STATEMENTS (BREAK, CONTINUE, PASS)
# ==========================================

# Q9: Use 'continue' to print numbers from 1 to 10 except multiples of 3.
print("Numbers 1-10 skipping multiples of 3:")
for i in range(1, 11):
    if i % 3 == 0:
        continue
    print(i, end=" ")
print()

# Q10: Use 'break' to stop searching a list once the target item is found.
items = [12, 45, 67, 89, 23, 90]
target = 89
found = False

for item in items:
    if item == target:
        found = True
        break

print(f"Target {target} found in list:", found)


# ==========================================
# 6. FOR-ELSE / WHILE-ELSE LOOPS
# ==========================================

# Q11: Check if a number is prime using a for-else loop.
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
        # Executes ONLY if loop completes without a 'break'
        print(f"{number} is a PRIME number (confirmed by for-else).")
