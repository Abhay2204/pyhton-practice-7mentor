# 06. Lists & Operations in Python

## 📌 Overview
Lists in Python are ordered, heterogeneous, mutable sequences. They are declared using square brackets `[]`.

---

## 🔑 Key Concepts

### 1. Adding Elements
- `.append(element)`: Adds a single element to the end of the list.
- `.insert(index, element)`: Inserts element at specified index position.
- `.extend(iterable)`: Appends all items from another iterable to the list.

```python
lst = [1, 2]
lst.append(3)         # [1, 2, 3]
lst.insert(1, 1.5)    # [1, 1.5, 2, 3]
lst.extend([4, 5])    # [1, 1.5, 2, 3, 4, 5]
```

### 2. Removing Elements
- `.pop([index])`: Removes and returns item at index (defaults to last item).
- `.remove(value)`: Removes the **first occurrence** of value (raises `ValueError` if not found).
- `del lst[index]`: Deletes item at specific index or slice.
- `.clear()`: Removes all items, leaving an empty list.

### 3. Ordering & Sorting
- `.sort(key=None, reverse=False)`: Sorts list **in-place**.
- `sorted(iterable)`: Returns a **new** sorted list without modifying original.
- `.reverse()`: Reverses list elements **in-place**.

### 4. List Comprehension
Concise syntax for creating lists: `[expression for item in iterable if condition]`
```python
evens = [x for x in range(10) if x % 2 == 0] # [0, 2, 4, 6, 8]
```
