"""
03. Python Operators - Code Examples
------------------------------------
Demonstrates short-circuiting, bitwise operations, identity vs equality, and precedence.
"""

# 1. Identity vs Equality
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("=== Identity (is) vs Equality (==) ===")
print(f"list1 == list2: {list1 == list2}") # True
print(f"list1 is list2: {list1 is list2}") # False
print(f"list1 is list3: {list1 is list3}") # True

# 2. Short-Circuit Logical Operators
print("\n=== Short-Circuit Evaluation ===")
def check_first():
    print("Evaluated first condition!")
    return False

def check_second():
    print("Evaluated second condition!")
    return True

print("Evaluating (check_first() and check_second()):")
res = check_first() and check_second() # check_second won't be called!

# 3. Bitwise Operators
print("\n=== Bitwise Operations ===")
m = 12 # 1100 in binary
n = 5  # 0101 in binary

print(f"12 & 5  = {m & n}")  # 0100 -> 4
print(f"12 | 5  = {m | n}")  # 1101 -> 13
print(f"12 ^ 5  = {m ^ n}")  # 1001 -> 9
print(f"12 << 2 = {m << 2}") # 48
print(f"12 >> 2 = {m >> 2}") # 3

# 4. Membership Check
print("\n=== Membership Check ===")
user = {"name": "Abhay", "role": "Admin"}
print("'name' in user:", "name" in user) # True
print("'Admin' in user.values():", "Admin" in user.values()) # True
