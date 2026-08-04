# 05. String Manipulation & Methods in Python

## 📌 Overview
Strings in Python are **immutable** sequences of Unicode characters. Once created, their elements cannot be changed in place.

---

## 🔑 Key Concepts

### 1. Indexing & Slicing Syntax
`string[start:stop:step]`
- **`start`**: Inclusive starting index (default `0`).
- **`stop`**: Exclusive stopping index (default `len(string)`).
- **`step`**: Stride size (negative step reverses direction).

```python
s = "Antigravity"
print(s[0:4])   # "Anti"
print(s[4:])    # "gravity"
print(s[::-1])  # "ytivargitnA" (Reversed string)
```

### 2. Built-in String Methods
- **Case Transformations**: `.upper()`, `.lower()`, `.title()`, `.swapcase()`, `.capitalize()`
- **Searching**: `.find(sub)` (returns `-1` if not found), `.index(sub)` (raises `ValueError`), `.count(sub)`, `.startswith(sub)`, `.endswith(sub)`
- **Cleaning & Modification**: `.strip()`, `.lstrip()`, `.rstrip()`, `.replace(old, new)`
- **Splitting & Joining**: `.split(sep)`, `.join(iterable)`
- **Inspection**: `.isdigit()`, `.isalpha()`, `.isalnum()`, `.isspace()`

### 3. Immutability Principle
String modification methods (like `.replace()` or `.upper()`) do **not** alter the original string in place; they return a **new** string object.
