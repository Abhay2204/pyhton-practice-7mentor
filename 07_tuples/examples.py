"""
07. Tuples & Immutability - Code Examples
------------------------------------------
Demonstrates single-element tuples, extended unpacking, nested tuple extraction, and slicing.
"""

# 1. Extended Unpacking
records = (101, "Laptop", 899.99, "Electronics", "In Stock")
id_, name, price, *metadata = records

print("=== Extended Unpacking ===")
print("ID:", id_)
print("Name:", name)
print("Price:", price)
print("Metadata Tail:", metadata)

# 2. Nested Tuple Unpacking
data = [(1, 2), (3, 4)]
(a, b), (c, d) = data
print("\nNested Unpacked:", a, b, c, d)

# 3. Item Removal via Slicing Workaround
basket = ("Mobile", "Mini car", "Jcb", "Ball")
print("\nOriginal Basket:", basket)
basket_without_mobile = basket[1:]
print("After Slicing out 'Mobile':", basket_without_mobile)
