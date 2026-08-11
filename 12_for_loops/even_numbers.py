"""
Print Even Numbers Between 1 to 50
----------------------------------
This script demonstrates multiple approaches to generate and print
even numbers between 1 and 50 using Python's 'for' loop.
"""

# ==========================================
# APPROACH 1: Using range() with Step = 2 (Best Practice)
# ==========================================
print("--- Approach 1: range(2, 51, 2) ---")
for num in range(2, 51, 2):
    print(num )
print("\n")


# ==========================================
# APPROACH 2: Using for Loop with if (Modulus Operator)
# ==========================================
print("--- Approach 2: for loop with if condition (num % 2 == 0) ---")
for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=" ")
print("\n")


# ==========================================
# APPROACH 3: List Comprehension
# ==========================================
print("--- Approach 3: List Comprehension ---")
even_list = [num for num in range(2, 51, 2)]
print("Even numbers list:", even_list)
print()


# ==========================================
# BONUS: Count and Sum of Even Numbers
# ==========================================
even_count = 0
even_sum = 0

for num in range(2, 51, 2):
    even_count += 1
    even_sum += num

print(f"Total even numbers between 1 and 50: {even_count}")
print(f"Sum of all even numbers between 1 and 50: {even_sum}")
