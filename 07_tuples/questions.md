# ❓ 07. Tuples & Immutability - Questions & Exercises

## 📝 Conceptual Questions

### Q1: Why are tuples preferred over lists in Python for dictionary keys?
**Answer:** Tuples are **immutable** (and thus hashable, provided all their elements are hashable), making them suitable as dictionary keys or set elements. Lists are mutable (unhashable) and cannot be dictionary keys.

### Q2: What happens if a tuple contains a mutable object like a list e.g. `t = (1, [2, 3])`?
**Answer:** The tuple structure itself is immutable (references cannot be reassigned), but the nested list inside the tuple **can still be modified in-place** (`t[1].append(4)` succeeds).

---

## 💻 Practical Exercises & Solutions

### Challenge 1: Swap Variables Using Tuple Packing/Unpacking
Swap two variables `a = 5` and `b = 10` in a single line.

**Solution:**
```python
a, b = 5, 10
a, b = b, a
print(f"a = {a}, b = {b}") # a = 10, b = 5
```

### Challenge 2: Sort List of Tuples by 2nd Element
Sort `students = [("Alice", 88), ("Bob", 95), ("Charlie", 78)]` by grade (descending).

**Solution:**
```python
students = [("Alice", 88), ("Bob", 95), ("Charlie", 78)]
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("Sorted Students:", sorted_students)
```
