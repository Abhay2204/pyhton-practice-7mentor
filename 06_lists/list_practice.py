"""
Python List Practice Questions
------------------------------
This file contains various basic-to-intermediate list practice questions 
covering creation, indexing, slicing, modification, removal, sorting, and aggregations.
"""

# ==========================================
# 1. LIST CREATION & INDEXING
# ==========================================

fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("3rd fruit:", fruits[2])
print("2nd fruit from end:", fruits[-2])


# ==========================================
# 2. LIST SLICING
# ==========================================

numbers = [10, 20, 30, 40, 50, 60, 70, 80]
print("First 3:", numbers[:3])
print("Index 3 to 6:", numbers[3:7])
print("Reversed numbers:", numbers[::-1])
print("Every 2nd number:", numbers[::2])


# ==========================================
# 3. ADDING ELEMENTS
# ==========================================

colors = ["red", "blue"]
colors.append("green")
print("After append:", colors)
colors.insert(1, "yellow")
print("After insert at 1:", colors)
colors.extend(["purple", "orange"])
print("After extend:", colors)


# ==========================================
# 4. REMOVING ELEMENTS
# ==========================================

animals = ["cat", "dog", "lion", "tiger", "dog", "elephant"]
animals.remove("dog")
print("After remove('dog'):", animals)
popped_animal = animals.pop()
print("Popped animal:", popped_animal)
print("After pop():", animals)
del animals[1]
print("After del index 1:", animals)
animals.clear()
print("After clear():", animals)


# ==========================================
# 5. SEARCHING & COUNTING
# ==========================================

scores = [85, 90, 75, 90, 100, 90, 80]
print("Count of 90:", scores.count(90))
print("Index of 100:", scores.index(100))
print("75 in scores?", 75 in scores)


# ==========================================
# 6. SORTING & REVERSING
# ==========================================

items = [42, 12, 88, 3, 25]
items.sort()
print("Sorted ascending:", items)
items.sort(reverse=True)
print("Sorted descending:", items)
items.reverse()
print("Reversed:", items)


# ==========================================
# 7. AGGREGATION & BUILT-IN FUNCTIONS
# ==========================================

val_list = [5, 12, 8, 20, 3]
print("Sum:", sum(val_list))
print("Min:", min(val_list))
print("Max:", max(val_list))
print("Length:", len(val_list))


# ==========================================
# 8. MINI CHALLENGES
# ==========================================

mix_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in mix_numbers if x % 2 == 0]
print("Even numbers list:", evens)

dup_list = [1, 2, 2, 3, 4, 4, 4, 5]
unique_list = list(set(dup_list))
print("Unique numbers list:", unique_list)
