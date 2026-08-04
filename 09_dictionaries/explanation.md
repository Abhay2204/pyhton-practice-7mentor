# 09. Dictionaries & Mapping Types in Python

## 📌 Overview
A Dictionary is an **ordered** (Python 3.7+), **mutable** collection of `key: value` pairs. Keys must be unique and hashable (immutable data types like `str`, `int`, `tuple`).

---

## 🔑 Key Concepts

### 1. Dictionary Access & `.get()` Safety
Accessing a missing key via `dict[key]` raises `KeyError`. Using `dict.get(key, default)` safely returns `None` or a custom fallback value.
```python
d = {"name": "Abhay", "age": 22}
print(d.get("name"))        # "Abhay"
print(d.get("salary", 0.0)) # 0.0 (Fallback, no KeyError)
```

### 2. Dictionary Modification & Operations
- `dict[key] = value`: Adds or updates a key-value pair.
- `dict.update(other_dict)`: Merges another dictionary or key-value sequence.
- `dict.pop(key[, default])`: Removes key and returns value.
- `dict.popitem()`: Removes and returns the last inserted key-value pair.
- `del dict[key]`: Deletes key-value pair.

### 3. Dictionary Iteration Methods
- `dict.keys()`: Returns a view object of dictionary keys.
- `dict.values()`: Returns a view object of dictionary values.
- `dict.items()`: Returns a view object of `(key, value)` tuples.

```python
for key, val in d.items():
    print(f"{key} -> {val}")
```

### 4. Dictionary Comprehension
Syntax: `{key_expr: val_expr for item in iterable if condition}`
```python
squared_even_map = {x: x**2 for x in range(1, 6) if x % 2 == 0}
# {2: 4, 4: 16}
```
