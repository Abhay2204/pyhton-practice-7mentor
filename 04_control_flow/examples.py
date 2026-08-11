"""
04. Control Flow - Code Examples
---------------------------------
Demonstrates leap year calculations (3 methods), for-else loops, factorials, and enumerate.
"""

# 1. Leap Year Calculation (3 Approaches)
year = 2024
print("=== 3 Leap Year Approaches ===")

# Approach 1: Built-in calendar module
import calendar
print("Approach 1 (calendar.isleap):", calendar.isleap(year))

# Approach 2: Step-by-step logic
if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False
print("Approach 2 (if-elif-else):", is_leap)

# Approach 3: Single-line conditional
is_leap_comb = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("Approach 3 (Boolean Formula):", is_leap_comb)

# 2. Prime Number Verification via `for-else`
print("\n=== Prime Verification (for-else) ===")
number = 29
for i in range(2, int(number**0.5) + 1):
    if number % i == 0:
        print(f"{number} is not prime")
        break
else:
    print(f"{number} is a PRIME number!")

# 3. Factorial using `while` loop
print("\n=== Factorial Calculation ===")
n = 6
fact = 1
temp = n
while temp > 0:
    fact *= temp
    temp -= 1
print(f"{n}! =", fact)




age = int(input("enter the value of age: "))
has_license = input("do you have license? (yes/no): ").strip().lower()

if age >= 18:
    if has_license == "yes" :
        print("ready to buy car")
    else:
        print("you are not ready to buy car")
else:
    print("you are so small")