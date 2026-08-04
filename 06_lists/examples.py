"""
06. Lists & Operations - Code Examples
---------------------------------------
Demonstrates list CRUD operations, list comprehensions, sorting, and aggregations.
"""

# 1. Modifying & Extending Lists
colors = ["red", "blue"]
colors.append("green")
colors.insert(1, "yellow")
colors.extend(["purple", "orange"])
print("=== Modified Colors List ===")
print(colors)

# 2. In-Place Sorting vs Built-in Sorted
scores = [42, 12, 88, 3, 25]
print("\nOriginal scores:", scores)
print("sorted(scores):", sorted(scores))
print("Original untouched:", scores)

scores.sort(reverse=True)
print("scores.sort(reverse=True):", scores)

# 3. List Comprehensions
squares_of_evens = [x**2 for x in range(1, 11) if x % 2 == 0]
print("\nSquares of evens (1 to 10):", squares_of_evens)

# 4. Aggregation
numbers = [10, 25, 5, 80, 45]
print("\n=== Aggregations ===")
print("Sum:", sum(numbers))
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Len:", len(numbers))
print("Average:", sum(numbers) / len(numbers))
