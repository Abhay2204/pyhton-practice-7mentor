# 02. Typecasting & Coercion in Python

## 📌 Overview
Typecasting (or Type Conversion) refers to changing an object from one data type to another. Python supports both **Implicit** type conversion (coercion performed automatically by the interpreter) and **Explicit** type conversion (typecasting performed manually by the programmer).

---

## 🔑 Key Concepts

### 1. Implicit Type Conversion
Python automatically promotes smaller data types to larger ones to prevent data loss.
```python
x = 10     # int
y = 2.5    # float
res = x + y # float (12.5) — automatically converted
```

### 2. Explicit Typecasting Functions
- `int(x, base=10)`: Converts to integer. Truncates floats.
- `float(x)`: Converts to floating point.
- `str(x)`: Converts object `x` into its string representation.
- `bool(x)`: Evaluates truthiness (`False` for `0`, `""`, `[]`, `{}`, `None`, `set()`; `True` otherwise).

### 3. Collection Typecasting
- `list(seq)`: Converts tuple, string, or set into a list.
- `tuple(seq)`: Converts list, string, or set into a tuple (useful for immutability).
- `set(seq)`: Removes duplicates and returns an unordered set.
- `dict(pairs)` or `dict(zip(keys, values))`: Converts pairs or zipped sequences to key-value mappings.

### 4. Base & ASCII Conversions
- `ord(char)`: Returns the integer ASCII/Unicode code point.
- `chr(code)`: Returns character from ASCII code point.
- `bin(x)`, `oct(x)`, `hex(x)`: Converts integer to binary (`0b`), octal (`0o`), and hex (`0x`) strings.
- `int(str, base)`: Converts base-N string back to base-10 integer.

---

## ⚠️ Important Rules & Edge Cases
1. `int("12.34")` raises a `ValueError`! Cast to `float` first: `int(float("12.34"))`.
2. Casting float to int (`int(12.89)`) **truncates** toward zero (`12`), whereas `round(12.89)` yields `13`.
