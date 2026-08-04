"""
Python Typecasting Practice Questions
-------------------------------------
This file contains practice questions covering implicit and explicit type 
casting concepts in Python (int, float, str, bool, list, tuple, set, dict, 
and base/ASCII conversions).
"""

# ==========================================
# 1. IMPLICIT TYPE CONVERSION
# ==========================================

num_int = 10
num_float = 5.5
result1 = num_int + num_float
print("Implicit Addition:", result1, "| Type:", type(result1))

result2 = 10 + True
print("Implicit Bool + Int:", result2, "| Type:", type(result2))


# ==========================================
# 2. PRIMITIVE TYPE CASTING (int, float, str, bool)
# ==========================================

str_val = "250"
num = int(str_val) + 50
print("Converted String to Int + 50:", num)

float_str = "45.75"
val_float = float(float_str)
print("Converted String to Float:", val_float)

price_str = "99.99"
price_int = int(float(price_str))
print("Float String to Int:", price_int)

val = 12.87
print("Truncated Int:", int(val))
print("Rounded Int  :", round(val))

age = 25
height = 5.9
message = "Age: " + str(age) + ", Height: " + str(height)
print(message)

print("bool(0):", bool(0))
print("bool(''):", bool(""))
print("bool([]):", bool([]))
print("bool(None):", bool(None))
print("bool(42):", bool(42))
print("bool('Python'):", bool("Python"))


# ==========================================
# 3. COLLECTION TYPE CASTING (list, tuple, set, dict)
# ==========================================

text = "Python"
print("List :", list(text))
print("Tuple:", tuple(text))
print("Set  :", set(text))

tup = ("apple", "banana")
lst = list(tup)
lst.append("cherry")
tup_updated = tuple(lst)
print("Updated Tuple:", tup_updated)

numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("Unique Numbers List:", unique_numbers)

pairs = [("a", 1), ("b", 2)]
d = dict(pairs)
print("Dict from Pairs:", d)

keys = ["name", "age"]
values = ["Alice", 25]
person_dict = dict(zip(keys, values))
print("Dict from Zip:", person_dict)


# ==========================================
# 4. ASCII & BASE CONVERSIONS
# ==========================================

print("ASCII of 'A':", ord('A'))
print("Char of 97  :", chr(97))

num_42 = 42
print("Binary     :", bin(num_42))
print("Octal      :", oct(num_42))
print("Hexadecimal:", hex(num_42))

print("Binary '1010' to Int:", int("1010", 2))
print("Hex '1A' to Int     :", int("1A", 16))


# ==========================================
# 5. MINI CHALLENGES
# ==========================================

price_input = "$149.99"
qty_input = "3"
clean_price = float(price_input.replace("$", ""))
qty = int(qty_input)
total = clean_price * qty
print("Total Cost:", total)

str_floats = ["10.5", "20.25", "30.75"]
float_list = [float(x) for x in str_floats]
total_sum = sum(float_list)
print("Float Sum:", total_sum)
print("Int Sum  :", int(total_sum))
