"""
02. Typecasting & Coercion - Code Examples
--------------------------------------------
Demonstrates primitive, collection, base, and ASCII conversions.
"""

# 1. Primitive Typecasting
price_str = "99.99"
price_int = int(float(price_str)) # 2-step casting required
print("Float String '99.99' to Int:", price_int)

# 2. Truthiness Evaluation
print("\n=== Truthiness ===")
values = [0, "", [], None, 42, "Python"]
for val in values:
    print(f"bool({repr(val)}): {bool(val)}")

# 3. Collection Transformations & Deduplication
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("\nDeduplicated List:", unique_numbers)

# 4. Dictionary from Zipped Sequences
keys = ["name", "role", "city"]
values = ["Abhay", "Developer", "Pune"]
user_profile = dict(zip(keys, values))
print("\nUser Profile Dict:", user_profile)

# 5. Base & ASCII Conversions
print("\n=== ASCII & Base Conversions ===")
print("ASCII of 'A':", ord('A'))
print("Character of 97:", chr(97))
print("Binary of 42:", bin(42))
print("Hex '1A' to Decimal:", int("1A", 16))
