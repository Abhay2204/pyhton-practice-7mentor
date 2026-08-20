# ---------------------------------------------
# SET FUNCTIONS PRACTICE
# ---------------------------------------------

# 1. Creating a set with range()
numbers = set(range(1, 6))
print("1. Initial Set using range(1, 6):", numbers)

# 2. add() - Add a single element
numbers.add(10)
print("\n2. After add(10):", numbers)

# 3. update() - Add multiple elements (list, range, etc.)
numbers.update([20, 30])
numbers.update(range(40, 43))
print("\n3. After update([20, 30]) and update(range(40, 43)):", numbers)

# 4. remove() - Remove a specific element (raises error if element not found)
numbers.remove(10)
print("\n4. After remove(10):", numbers)

# 5. discard() - Remove an element safely (NO error if element not found)
numbers.discard(99)  # 99 is not in the set, but won't crash
numbers.discard(20)
print("\n5. After discard(99) and discard(20):", numbers)

# 6. pop() - Remove and return a random element
removed_item = numbers.pop()
print(f"\n6. Popped item: {removed_item}")
print("   Set after pop():", numbers)

# 7. len() and in (membership test)
print(f"\n7. Total elements (len): {len(numbers)}")
print("   Is 30 in set?", 30 in numbers)

# 8. Set Operations (union, intersection, difference)
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("\n8. Set A:", set_a)
print("   Set B:", set_b)
print("   Union (A | B):", set_a.union(set_b))
print("   Intersection (A & B):", set_a.intersection(set_b))
print("   Difference (A - B):", set_a.difference(set_b))

# 9. copy() - Shallow copy of set
new_set = numbers.copy()
print("\n9. Copied Set:", new_set)

# 10. clear() - Remove all elements
numbers.clear()
print("\n10. After clear():", numbers)
