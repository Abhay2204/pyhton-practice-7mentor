"""
01. Python Basics & Fundamentals - Code Examples
------------------------------------------------
Demonstrates variables, primitive types, string formatting, and simple input/output.
"""

# 1. Variable Assignment & Type Inspection
age = 21
height = 5.11
name = "Abhay"
is_enrolled = True

print("=== Variable Types ===")
print(f"name: {name} (Type: {type(name).__name__})")
print(f"age: {age} (Type: {type(age).__name__})")
print(f"height: {height} (Type: {type(height).__name__})")
print(f"is_enrolled: {is_enrolled} (Type: {type(is_enrolled).__name__})")

# 2. String Concatenation & F-Strings
first_name = "ANNURUDH"
last_name = "JADAV"

full_name = first_name + " " + last_name
print("\n=== Concatenation & Formatting ===")
print("Concatenated Name:", full_name)

product = "Gaming Monitor"
price = 249.99
quantity = 3
total_price = price * quantity

print(f"Product: {product}")
print(f"Unit Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total Amount: ${total_price:.2f}")
