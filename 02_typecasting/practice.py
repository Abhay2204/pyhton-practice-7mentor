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

# Q1: Add an integer (10) and a float (5.5). Print the result and its type.
num_int = 10
num_float = 5.5
result1 = num_int + num_float
print("Implicit Addition:", result1, "| Type:", type(result1))

# Q2: Add an integer (10) and a boolean (True). Print the result and its type.
result2 = 10 + True
print("Implicit Bool + Int:", result2, "| Type:", type(result2))


# ==========================================
# 2. PRIMITIVE TYPE CASTING (int, float, str, bool)
# ==========================================

# Q3: Convert string "250" to an integer and add 50 to it.
str_val = "250"
num = int(str_val) + 50
print("Converted String to Int + 50:", num)

# Q4: Convert string "45.75" to a float.
float_str = "45.75"
val_float = float(float_str)
print("Converted String to Float:", val_float)

# Q5: Convert float string "99.99" to an integer (Requires 2-step casting).
price_str = "99.99"
price_int = int(float(price_str))
print("Float String to Int:", price_int)

# Q6: Convert float 12.87 to an integer (truncation) vs round(12.87).
val = 12.87
print("Truncated Int:", int(val))
print("Rounded Int  :", round(val))

# Q7: Convert age (25) and height (5.9) to strings and concatenate into a message.
age = 25
height = 5.9
message = "Age: " + str(age) + ", Height: " + str(height)
print(message)

# Q8: Evaluate and print boolean truthiness of 0, "", [], None, 42, and "Python".
print("bool(0):", bool(0))
print("bool(''):", bool(""))
print("bool([]):", bool([]))
print("bool(None):", bool(None))
print("bool(42):", bool(42))
print("bool('Python'):", bool("Python"))


# ==========================================
# 3. COLLECTION TYPE CASTING (list, tuple, set, dict)
# ==========================================

# Q9: Convert string "Python" to a list of characters, tuple, and set.
text = "Python"
print("List :", list(text))
print("Tuple:", tuple(text))
print("Set  :", set(text))

# Q10: Modify immutable tuple ("apple", "banana") by casting to list, adding "cherry", and converting back.
tup = ("apple", "banana")
lst = list(tup)
lst.append("cherry")
tup_updated = tuple(lst)
print("Updated Tuple:", tup_updated)

# Q11: Remove duplicate numbers from list [1, 2, 2, 3, 4, 4, 5] using set casting.
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("Unique Numbers List:", unique_numbers)

# Q12: Convert key-value tuples [("a", 1), ("b", 2)] into a dictionary.
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)
print("Dict from Pairs:", d)

# Q13: Convert keys=["name", "age"] and values=["Alice", 25] into dictionary using zip().
keys = ["name", "age"]
values = ["Alice", 25]
person_dict = dict(zip(keys, values))
print("Dict from Zip:", person_dict)


# ==========================================
# 4. ASCII & BASE CONVERSIONS
# ==========================================

# Q14: Find ASCII code of 'A' using ord() and character for code 97 using chr().
print("ASCII of 'A':", ord('A'))
print("Char of 97  :", chr(97))

# Q15: Convert 42 to binary, octal, hex using bin(), oct(), hex().
num_42 = 42
print("Binary     :", bin(num_42))
print("Octal      :", oct(num_42))
print("Hexadecimal:", hex(num_42))

# Q16: Convert binary string "1010" and hex string "1A" to decimal int.
print("Binary '1010' to Int:", int("1010", 2))
print("Hex '1A' to Int     :", int("1A", 16))


# ==========================================
# 5. MINI CHALLENGES
# ==========================================

# Q17: Clean user input "$149.99" to float, convert string quantity "3" to int, and print total cost.
price_input = "$149.99"
qty_input = "3"
clean_price = float(price_input.replace("$", ""))
qty = int(qty_input)
total = clean_price * qty
print("Total Cost:", total)

# Q18: Convert float strings ["10.5", "20.25", "30.75"] to float, calculate sum, cast to int.
str_floats = ["10.5", "20.25", "30.75"]
float_list = [float(x) for x in str_floats]
total_sum = sum(float_list)
print("Float Sum:", total_sum)
print("Int Sum  :", int(total_sum))
