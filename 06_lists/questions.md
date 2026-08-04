# ❓ 06. Lists & Operations - Questions & Exercises

## 📝 Conceptual Questions

### Q1: What is the difference between `.append()` and `.extend()`?
**Answer:**
- `.append(x)` adds `x` as a **single element** at the end (e.g. appending `[3, 4]` creates a nested list `[1, 2, [3, 4]]`).
- `.extend(iterable)` iterates over `iterable` and appends **each item individually** (`[1, 2, 3, 4]`).

### Q2: What is the difference between `list.sort()` and `sorted(list)`?
**Answer:**
- `list.sort()` sorts the list **in-place** and returns `None`.
- `sorted(list)` returns a **new sorted list** and leaves the original list unmodified.

---

## 💻 Practical Exercises & Solutions

### Challenge 1: Flatten 2D Matrix
Flatten `matrix = [[1, 2], [3, 4], [5, 6]]` using a list comprehension.

**Solution:**
```python
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print("Flat List:", flat) # [1, 2, 3, 4, 5, 6]
```

### Challenge 2: Second Largest Element
Find the 2nd largest element in a list of integers `[10, 20, 4, 45, 99, 99, 45]`.

**Solution:**
```python
numbers = [10, 20, 4, 45, 99, 99, 45]
unique_sorted = sorted(list(set(numbers)), reverse=True)
second_largest = unique_sorted[1]
print("Second Largest:", second_largest) # 45
```
