"""
Python Set Practice Questions
------------------------------
This file contains practice questions covering set creation, uniqueness,
adding/removing elements, mathematical set operations (union, intersection,
difference, symmetric difference), subset relations, and frozensets.

Try solving each question or run this file to verify the solutions.
"""

# ==========================================
# 1. SET CREATION & UNIQUENESS
# ==========================================

# Q1: Create a set named 'colors' containing "red", "green", "blue".
colors = {"red", "green", "blue"}
print("Colors Set:", colors)

# Q2: Note that empty curly braces {} create a dictionary! Create a true empty set using set().
empty_dict = {}
empty_set = set()
print("Type of {}:", type(empty_dict))
print("Type of set():", type(empty_set))

# Q3: Use a set to automatically remove duplicates from a list: [1, 2, 2, 3, 4, 4, 4, 5].
numbers_list = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers_list)
print("Unique numbers set:", unique_numbers)


# ==========================================
# 2. ADDING & REMOVING ELEMENTS
# ==========================================

fruits = {"apple", "banana"}

# Q4: Add a single element "cherry" to 'fruits' using .add().
fruits.add("cherry")
print("After add():", fruits)

# Q5: Add multiple elements ["date", "elderberry"] to 'fruits' using .update().
fruits.update(["date", "elderberry"])
print("After update():", fruits)

# Q6: Difference between .remove() and .discard():
# .remove() raises KeyError if item doesn't exist, .discard() fails silently.
fruits.discard("mango")  # Does not raise error even though "mango" is missing
print("After discard('mango'):", fruits)

fruits.remove("apple")   # Removes "apple"
print("After remove('apple'):", fruits)

# Q7: Remove and return an arbitrary element using .pop().
popped_item = fruits.pop()
print("Popped item:", popped_item)
print("Remaining set:", fruits)


# ==========================================
# 3. SET MATHEMATICAL OPERATIONS
# ==========================================

set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

# Q8: Find the Union (all unique elements from both sets) using | and .union().
union_set = set_A | set_B
print("Union (A | B):", union_set)

# Q9: Find the Intersection (common elements) using & and .intersection().
intersection_set = set_A & set_B
print("Intersection (A & B):", intersection_set)

# Q10: Find the Difference (elements in A but not in B) using - and .difference().
diff_A_B = set_A - set_B
print("Difference (A - B):", diff_A_B)

# Q11: Find the Symmetric Difference (elements in A or B, but NOT both) using ^ and .symmetric_difference().
sym_diff = set_A ^ set_B
print("Symmetric Difference (A ^ B):", sym_diff)


# ==========================================
# 4. SUBSETS & SUPERSETS
# ==========================================

X = {1, 2, 3}
Y = {1, 2, 3, 4, 5}
Z = {6, 7}

# Q12: Check if X is a subset of Y using .issubset() or <=.
print("X is subset of Y:", X.issubset(Y))

# Q13: Check if Y is a superset of X using .issuperset() or >=.
print("Y is superset of X:", Y.issuperset(X))

# Q14: Check if X and Z have no elements in common using .isdisjoint().
print("X and Z are disjoint:", X.isdisjoint(Z))


# ==========================================
# 5. FROZEN SETS (IMMUTABLE SETS)
# ==========================================

# Q15: Create an immutable set using frozenset(). (Useful as dictionary keys or set elements)
frozen_A = frozenset([10, 20, 30])
print("Frozenset:", frozen_A, "Type:", type(frozen_A))
# frozen_A.add(40)  # AttributeError: 'frozenset' object has no attribute 'add'
