"""
Module 12: Python For Loop Demonstrations & Examples
---------------------------------------------------
This script demonstrates the syntax, usage patterns, and best practices
of 'for' loops in Python.
"""

# ==========================================
# 1. BASIC FOR LOOPS WITH RANGE()
# ==========================================
print("--- 1. Basic range() Demonstrations ---")
print("range(5) ->", end=" ")
for i in range(5):
    print(i, end=" ")
print()

print("range(2, 7) ->", end=" ")
for i in range(2, 7):
    print(i, end=" ")
print()

print("range(1, 10, 2) (Odd numbers) ->", end=" ")
for i in range(1, 10, 2):
    print(i, end=" ")
print()

print("range(5, 0, -1) (Reverse countdown) ->", end=" ")
for i in range(5, 0, -1):
    print(i, end=" ")
print("\n")


# ==========================================
# 2. ITERATING DATA STRUCTURES
# ==========================================
print("--- 2. Iterating Collections ---")
# String
name = "PYTHON"
print("Characters in 'PYTHON':", end=" ")
for char in name:
    print(char, end="-")
print()

# List
technologies = ["Python", "FastAPI", "PostgreSQL", "Docker"]
print("Tech Stack:")
for tech in technologies:
    print(f" -> {tech}")

# Dictionary
student_scores = {"Abhay": 94, "Rahul": 88, "Priya": 91}
print("Scores using .items():")
for student, score in student_scores.items():
    print(f"  * {student}: {score}/100")
print()


# ==========================================
# 3. ENUMERATE & ZIP
# ==========================================
print("--- 3. enumerate() and zip() ---")
colors = ["Red", "Green", "Blue", "Yellow"]
print("Enumerated Colors:")
for index, color in enumerate(colors, start=1):
    print(f"  [{index}] {color}")

names = ["Alice", "Bob", "Charlie"]
ages = [24, 27, 22]
cities = ["Pune", "Mumbai", "Bangalore"]

print("\nZipped Profile Records:")
for name, age, city in zip(names, ages, cities):
    print(f"  Name: {name:7} | Age: {age} | City: {city}")
print()


# ==========================================
# 4. LOOP CONTROL: BREAK, CONTINUE, PASS
# ==========================================
print("--- 4. Loop Controls (break, continue, pass) ---")
print("Break at 5 (range 1-10):", end=" ")
for n in range(1, 11):
    if n == 5:
        break
    print(n, end=" ")
print()

print("Continue on multiples of 3 (range 1-10):", end=" ")
for n in range(1, 11):
    if n % 3 == 0:
        continue
    print(n, end=" ")
print("\n")


# ==========================================
# 5. FOR-ELSE CONSTRUCT
# ==========================================
print("--- 5. For-Else Search Demonstration ---")
numbers = [10, 20, 30, 40, 50]
target = 35

print(f"Searching for {target} in {numbers}:")
for val in numbers:
    if val == target:
        print(f"  -> Found {target}!")
        break
else:
    print(f"  -> Value {target} was NOT found in list.")
print()


# ==========================================
# 6. NESTED LOOPS & PATTERNS
# ==========================================
print("--- 6. Nested Loop Star Triangle ---")
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
print()


# ==========================================
# 7. PRIME NUMBER CHECKER ALGORITHM
# ==========================================
print("--- 7. Prime Number Check using for-else ---")
test_number = 29
if test_number < 2:
    print(f"{test_number} is NOT prime.")
else:
    for divisor in range(2, int(test_number ** 0.5) + 1):
        if test_number % divisor == 0:
            print(f"{test_number} is NOT prime (divisible by {divisor}).")
            break
    else:
        print(f"{test_number} is a PRIME NUMBER!")
