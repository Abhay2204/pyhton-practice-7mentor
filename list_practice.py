"""
Python List Practice Questions
------------------------------
This file contains various basic-to-intermediate list practice questions 
covering all major list concepts in Python.

Try solving each question below by writing your code where indicated.
"""

# ==========================================
# 1. LIST CREATION & INDEXING
# ==========================================

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Q1: Print the first and the last element of the list 'fruits'.
# Your code here:
print(fruits[0])
print(fruits[-1])

# Q2: Print the 3rd element (index 2) of the list 'fruits'.
# Your code here:
print(fruits[2])

# Q3: Print the 2nd element from the end using negative indexing.
# Your code here:
print(fruits[-2])

# ==========================================
# 2. LIST SLICING
# ==========================================

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

# Q4: Slice and print the first 3 numbers ([10, 20, 30]).
# Your code here:
print(numbers[:3])

# Q5: Slice and print numbers from index 3 to 6 ([40, 50, 60, 70]).
# Your code here:
print(numbers[3:7])

# Q6: Reverse the list 'numbers' using slicing.
# Your code here:
print(numbers[::-1])

# Q7: Print every 2nd number in 'numbers' starting from index 0 ([10, 30, 50, 70]).
# Your code here:
print(numbers[::2])

# ==========================================
# 3. ADDING ELEMENTS
# ==========================================

colors = ["red", "blue"]

# Q8: Add "green" to the end of the list 'colors' using .append().
# Your code here:
colors.append("green")
print(colors)

# Q9: Insert "yellow" at index 1 in the list 'colors' using .insert().
# Your code here:
colors.insert(1,"yellow")
print(colors)

# Q10: Add multiple items ["purple", "orange"] to 'colors' using .extend().
# Your code here:
colors.extend(["purple","orange"])
print(colors)


# ==========================================
# 4. REMOVING ELEMENTS
# ==========================================

animals = ["cat", "dog", "lion", "tiger", "dog", "elephant"]

# Q11: Remove the first occurrence of "dog" using .remove().
# Your code here:
animals.remove("dog")
print(animals)

# Q12: Remove and return the last element of 'animals' using .pop().
# Your code here:
animals.pop()
print(animals)


# Q13: Delete the element at index 1 using the 'del' statement.
# Your code here:
del animals[1]
print(animals)

# Q14: Clear all elements from 'animals' using .clear().
# Your code here:
animals.clear()
print(animals)

# ==========================================
# 5. SEARCHING & COUNTING
# ==========================================

scores = [85, 90, 75, 90, 100, 90, 80]

# Q15: Count how many times 90 appears in the list 'scores'.
# Your code here:
print(scores.count(90))

# Q16: Find the index position of the value 100 in 'scores'.
# Your code here:
print(scores.index(100))

# Q17: Check if the value 75 exists in 'scores' (returns True/False using 'in').
# Your code here:
print(75 in scores)
# ==========================================
# 6. SORTING & REVERSING
# ==========================================

items = [42, 12, 88, 3, 25]

# Q18: Sort the list 'items' in ascending order in-place using .sort().
# Your code here:
items.sort()
print(items)

# Q19: Sort the list 'items' in descending order in-place.
# Your code here:
items.sort(reverse=True)
print(items)


# Q20: Reverse the order of elements in 'items' using .reverse().
# Your code here:
items.reverse()
print(items)
# ==========================================
# 7. AGGREGATION & BUILT-IN FUNCTIONS
# ==========================================

val_list = [5, 12, 8, 20, 3]

# Q21: Find and print the sum of all elements in 'val_list' using sum().
# Your code here:
print(sum(val_list))

# Q22: Find and print the minimum (min) and maximum (max) values in 'val_list'.
# Your code here:
print(min(val_list))
print(max(val_list))


# Q23: Print the total length (number of items) of 'val_list' using len().
# Your code here:
print(len(val_list))

# ==========================================
# 8. MINI CHALLENGES
# ==========================================

# Q24: Given the list below, create a new list containing only the EVEN numbers.
mix_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Your code here:
print(mix_numbers[1::2])

# Q25: Remove duplicate items from the list below and print the unique list.
dup_list = [1, 2, 2, 3, 4, 4, 4, 5]
# Your code here:
unique_list = list(set(dup_list))
print(unique_list)
