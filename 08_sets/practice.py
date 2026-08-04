"""
Python Set Practice Questions
------------------------------
This file contains practice questions covering set creation, uniqueness,
adding/removing elements, mathematical set operations, subsets, and frozensets.
"""

# ==========================================
# 1. SET CREATION & UNIQUENESS
# ==========================================

colors = {"red", "green", "blue"}
print("Colors Set:", colors)

empty_dict = {}
empty_set = set()
print("Type of {}:", type(empty_dict))
print("Type of set():", type(empty_set))

numbers_list = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers_list)
print("Unique numbers set:", unique_numbers)


# ==========================================
# 2. ADDING & REMOVING ELEMENTS
# ==========================================

fruits = {"apple", "banana"}
fruits.add("cherry")
print("After add():", fruits)

fruits.update(["date", "elderberry"])
print("After update():", fruits)

fruits.discard("mango")
print("After discard('mango'):", fruits)

fruits.remove("apple")
print("After remove('apple'):", fruits)

popped_item = fruits.pop()
print("Popped item:", popped_item)
print("Remaining set:", fruits)


# ==========================================
# 3. SET MATHEMATICAL OPERATIONS
# ==========================================

set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

union_set = set_A | set_B
print("Union (A | B):", union_set)

intersection_set = set_A & set_B
print("Intersection (A & B):", intersection_set)

diff_A_B = set_A - set_B
print("Difference (A - B):", diff_A_B)

sym_diff = set_A ^ set_B
print("Symmetric Difference (A ^ B):", sym_diff)


# ==========================================
# 4. SUBSETS & SUPERSETS
# ==========================================

X = {1, 2, 3}
Y = {1, 2, 3, 4, 5}
Z = {6, 7}

print("X is subset of Y:", X.issubset(Y))
print("Y is superset of X:", Y.issuperset(X))
print("X and Z are disjoint:", X.isdisjoint(Z))


# ==========================================
# 5. FROZENSET EXERCISE
# ==========================================

frozen = frozenset([10, 20, 30])
print("Frozenset:", frozen, "| Type:", type(frozen))
