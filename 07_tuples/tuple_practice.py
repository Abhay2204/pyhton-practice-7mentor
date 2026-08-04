"""
Python Tuple Practice Questions
--------------------------------
This file contains practice questions covering tuple creation, slicing, immutability,
packing, extended unpacking, tuple methods, and tuple removal workarounds.
"""

# ==========================================
# 1. TUPLE CREATION & INDEXING
# ==========================================

fruits = ("apple", "banana", "cherry", "date", "elderberry")
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

single_element_tuple = ("python",)
print("Single Element Tuple:", single_element_tuple, "| Type:", type(single_element_tuple))

print("3rd fruit:", fruits[2])


# ==========================================
# 2. TUPLE SLICING
# ==========================================

numbers = (10, 20, 30, 40, 50, 60, 70, 80)
print("First 3 numbers:", numbers[:3])
print("Index 2 to 5:", numbers[2:6])
print("Reversed tuple:", numbers[::-1])
print("Every 2nd number:", numbers[::2])


# ==========================================
# 3. TUPLE IMMUTABILITY & MODIFICATION WORKAROUNDS
# ==========================================

colors = ("red", "green", "blue")
colors_list = list(colors)
colors_list.append("yellow")
colors = tuple(colors_list)
print("Updated Colors Tuple:", colors)

combined = (1, 2, 3) + (4, 5, 6)
print("Combined Tuple:", combined)

repeated = ("echo",) * 3
print("Repeated Tuple:", repeated)


# ==========================================
# 4. TUPLE PACKING & UNPACKING
# ==========================================

person = ("John", 25, "Engineer")
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")

data = (100, 200, 300, 400, 500)
head, *tail = data
print("Head:", head)
print("Tail:", tail)


# ==========================================
# 5. TUPLE METHODS & BUILT-IN FUNCTIONS
# ==========================================

sample_tuple = (5, 2, 8, 2, 9, 2, 1)
print("Count of 2:", sample_tuple.count(2))
print("Index of 8:", sample_tuple.index(8))
print("Length of sample tuple:", len(sample_tuple))
