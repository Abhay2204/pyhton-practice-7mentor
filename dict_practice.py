"""
Python Dictionaries & Sets Practice Questions
----------------------------------------------
This file contains practice questions covering essential Python Dictionary 
and Set operations. Write your answers directly under each question prompt.
"""

# ==========================================
# 1. DICTIONARY CREATION & ACCESSING
# ==========================================

student = {
    "name": "Alex",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics"]
}

# Q1: Print the value of the key 'name'.
# Your code here:


# Q2: Access and print the key 'age' using the .get() method.
# Your code here:


# Q3: Access and print the 2nd course ("Physics") from the 'courses' list inside the dictionary.
# Your code here:


# ==========================================
# 2. DICTIONARY MODIFICATION & METHODS
# ==========================================

# Q4: Add a new key-value pair 'city': 'New York' to 'student'.
# Your code here:


# Q5: Update the 'age' of 'student' to 21.
# Your code here:


# Q6: Remove the key 'grade' using .pop() and print the removed value.
# Your code here:


# Q7: Print all the keys of 'student' using .keys().
# Your code here:


# Q8: Print all the values of 'student' using .values().
# Your code here:


# Q9: Loop through 'student' and print key-value pairs using .items().
# Your code here:


# ==========================================
# 3. SET CREATION & BASIC OPERATIONS
# ==========================================

colors_set = {"red", "green", "blue"}

# Q10: Add "yellow" to 'colors_set' using .add().
# Your code here:


# Q11: Add multiple colors ["purple", "orange"] using .update().
# Your code here:


# Q12: Remove "red" from 'colors_set' using .remove() or .discard().
# Your code here:


# Q13: Check if "green" exists in 'colors_set' (returns True/False).
# Your code here:


# ==========================================
# 4. SET MATHEMATICAL OPERATIONS
# ==========================================

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Q14: Find and print the UNION of set_a and set_b (all unique elements from both).
# Your code here:


# Q15: Find and print the INTERSECTION of set_a and set_b (common elements).
# Your code here:


# Q16: Find elements in set_a that are NOT in set_b (DIFFERENCE).
# Your code here:


# Q17: Find elements that are in set_a OR set_b, but NOT in both (SYMMETRIC DIFFERENCE).
# Your code here:


# ==========================================
# 5. MINI CHALLENGES
# ==========================================

# Q18: Count the frequency of each word in the list below using a dictionary.
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
# Hint: word_counts = {}
# Your code here:


# Q19: Given the list with duplicates below, convert it to a set to remove duplicates, 
# then check if its length is smaller than the original list length.
raw_ids = [101, 102, 103, 101, 104, 102]
# Your code here:

