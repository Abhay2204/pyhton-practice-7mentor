"""
Module 12: Python For Loop Practice Workbook
--------------------------------------------
Practice exercises covering range(), accumulators, string processing,
patterns, and algorithmic problems using for loops.
"""

# ==========================================
# 1. ACCUMULATOR: SUM OF NUMBERS (1 to N)
# ==========================================
n = 10
total_sum = 0
for i in range(1, n + 1):
    total_sum += i
print(f"Sum of numbers 1 to {n}: {total_sum}")


# ==========================================
# 2. FACTORIAL COMPUTATION
# ==========================================
num = 6
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(f"Factorial of {num}: {factorial}")


# ==========================================
# 3. COUNT VOWELS & CONSONANTS
# ==========================================
sentence = "Learn Python Programming at 7Mentor"
vowels_count = 0
consonants_count = 0

for char in sentence.lower():
    if char.isalpha():
        if char in "aeiou":
            vowels_count += 1
        else:
            consonants_count += 1

print(f"Sentence: '{sentence}'")
print(f"Vowels: {vowels_count} | Consonants: {consonants_count}")


# ==========================================
# 4. REVERSE A STRING USING A FOR LOOP
# ==========================================
original = "Hello Python"
reversed_str = ""
for char in original:
    reversed_str = char + reversed_str
print(f"Original: '{original}' -> Reversed: '{reversed_str}'")


# ==========================================
# 5. FIND MAXIMUM & MINIMUM IN A LIST
# ==========================================
scores = [45, 88, 12, 99, 74, 63, 102, 5]
max_val = scores[0]
min_val = scores[0]

for score in scores:
    if score > max_val:
        max_val = score
    if score < min_val:
        min_val = score

print(f"Scores list: {scores}")
print(f"Maximum: {max_val} | Minimum: {min_val}")


# ==========================================
# 6. PYRAMID PATTERN PRINTING
# ==========================================
print("\n--- Pyramid Star Pattern ---")
rows = 5
for i in range(1, rows + 1):
    # Print leading spaces
    print(" " * (rows - i), end="")
    # Print stars
    print("* " * i)


# ==========================================
# 7. NUMBER SQUARE PATTERN
# ==========================================
print("\n--- Number Grid ---")
size = 4
for i in range(1, size + 1):
    for j in range(1, size + 1):
        print(f"{i * j:2d}", end=" ")
    print()
