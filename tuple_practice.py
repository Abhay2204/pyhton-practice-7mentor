"""
Python Tuple Practice Questions
--------------------------------
This file contains various basic-to-advanced tuple practice questions 
covering all major tuple concepts in Python.

Try solving each question below or run this file to verify the solutions.
"""

# ==========================================
# 1. TUPLE CREATION & INDEXING
# ==========================================

# Q1: Create a tuple named 'fruits' containing "apple", "banana", "cherry", "date", "elderberry".
fruits = ("apple", "banana", "cherry", "date", "elderberry")
print("Fruits Tuple:", fruits)

# Q2: Print the first and the last element of the tuple 'fruits'.
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Q3: Create a single-element tuple containing the string "python". (Remember the trailing comma!)
single_element_tuple = ("python",)
print("Single Element Tuple:", single_element_tuple, "Type:", type(single_element_tuple))

# Q4: Print the 3rd element (index 2) of 'fruits'.
print("3rd fruit:", fruits[2])


# ==========================================
# 2. TUPLE SLICING
# ==========================================

numbers = (10, 20, 30, 40, 50, 60, 70, 80)

# Q5: Slice and print the first 3 numbers ((10, 20, 30)).
print("First 3 numbers:", numbers[:3])

# Q6: Slice and print numbers from index 2 to 5 ((30, 40, 50, 60)).
print("Index 2 to 5:", numbers[2:6])

# Q7: Reverse the tuple 'numbers' using slicing.
print("Reversed tuple:", numbers[::-1])

# Q8: Print every 2nd number starting from index 0 ((10, 30, 50, 70)).
print("Every 2nd number:", numbers[::2])


# ==========================================
# 3. TUPLE IMMUTABILITY & MODIFICATION WORKAROUNDS
# ==========================================

colors = ("red", "green", "blue")

# Q9: Tuples are immutable! Convert 'colors' into a list, add "yellow", and convert back to a tuple.
colors_list = list(colors)
colors_list.append("yellow")
colors = tuple(colors_list)
print("Updated Colors Tuple:", colors)

# Q10: Concatenate two tuples: (1, 2, 3) and (4, 5, 6) using the '+' operator.
combined = (1, 2, 3) + (4, 5, 6)
print("Combined Tuple:", combined)

# Q11: Repeat a tuple ("echo",) 3 times using the '*' operator.
repeated = ("echo",) * 3
print("Repeated Tuple:", repeated)


# ==========================================
# 4. TUPLE PACKING & UNPACKING
# ==========================================

# Q12: Pack three values ("John", 25, "Engineer") into a tuple named 'person'.
person = ("John", 25, "Engineer")

# Q13: Unpack 'person' into variables 'name', 'age', and 'profession', then print them.
name, age, profession = person
print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Q14: Use extended unpacking (*) to extract the first element into 'head' and remaining elements into 'tail'.
data = (100, 200, 300, 400, 500)
head, *tail = data
print("Head:", head)
print("Tail:", tail)


# ==========================================
# 5. TUPLE METHODS & BUILT-IN FUNCTIONS
# ==========================================

sample_tuple = (5, 2, 8, 2, 9, 2, 1)

# Q15: Count how many times the number 2 appears in 'sample_tuple' using .count().
count_twos = sample_tuple.count(2)
print("Count of 2:", count_twos)

# Q16: Find the index of the first occurrence of the number 8 using .index().
index_of_eight = sample_tuple.index(8)
print("Index of 8:", index_of_eight)

# Q17: Find length, min, max, and sum of 'sample_tuple'.
print("Length:", len(sample_tuple))
print("Minimum:", min(sample_tuple))
print("Maximum:", max(sample_tuple))
print("Sum:", sum(sample_tuple))

# Q18: Get a sorted list from 'sample_tuple' using sorted().
sorted_list = sorted(sample_tuple)
print("Sorted list:", sorted_list)


# ==========================================
# 6. NESTED TUPLES & ITERATION
# ==========================================

nested_tuple = ((1, 2), (3, 4), (5, 6))

# Q19: Access and print the value 4 from 'nested_tuple'.
print("Accessing 4:", nested_tuple[1][1])

# Q20: Iterate over 'nested_tuple' and print the sum of each sub-tuple.
for sub in nested_tuple:
    print(f"Sum of {sub} is {sum(sub)}")
