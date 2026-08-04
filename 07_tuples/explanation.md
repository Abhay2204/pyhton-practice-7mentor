# 07. Tuples & Immutability in Python

## 📌 Overview
Tuples are ordered, **immutable** collections declared with parentheses `()`. Once created, items cannot be added, removed, or modified.

---

## 🔑 Key Concepts

### 1. Single-Element Tuples
To define a tuple with a single element, a **trailing comma** `,` is mandatory!
```python
t1 = ("python")  # <class 'str'> (NOT a tuple!)
t2 = ("python",) # <class 'tuple'>
```

### 2. Immutability & Modification Workarounds
Since tuples cannot be modified in place:
- **Workaround**: Convert to list -> Modify list -> Convert back to tuple.
- **Concatenation**: Combine tuples using `+` (creates a new tuple object).

### 3. Packing & Extended Unpacking
Assigning multiple values to a tuple is **packing**. Extracting tuple values into separate variables is **unpacking**.
```python
# Packing
person = ("Abhay", 22, "Pune")

# Unpacking
name, age, city = person

# Extended Unpacking with * wildcard
head, *tail = (1, 2, 3, 4, 5) # head=1, tail=[2, 3, 4, 5]
```

### 4. Tuple Methods
Tuples only have two built-in methods:
- `.count(x)`: Returns the number of occurrences of `x`.
- `.index(x)`: Returns the index of the first occurrence of `x`.
