# 01. Python Basics & Fundamentals

## 📌 Overview
Python is a dynamically typed, high-level, interpreted programming language known for its clear syntax and readability.

---

## 🔑 Key Concepts

### 1. Variables & Dynamic Typing
In Python, variables are created when you assign a value to them using the `=` assignment operator. Python dynamically infers the type at runtime.
```python
x = 10         # int
name = "Abhay" # str
gpa = 3.9      # float
is_active = True # bool
```

### 2. Primitive Data Types
- **Integer (`int`)**: Whole numbers (positive, negative, zero) e.g., `42`, `-7`.
- **Floating Point (`float`)**: Real numbers with decimals e.g., `3.14159`, `-0.01`.
- **String (`str`)**: Sequence of characters enclosed in single, double, or triple quotes e.g., `"Hello"`, `'Python'`.
- **Boolean (`bool`)**: Truth values `True` or `False`.

### 3. Input & Output (`print` & `input`)
- `print(*objects, sep=' ', end='\n')`: Outputs text/variables to standard output.
- `input(prompt)`: Accepts user input from the console (always returns a `str`).

### 4. F-String Formatting
Introduced in Python 3.6, formatted string literals (f-strings) provide a concise way to embed expressions inside string literals.
```python
item = "Laptop"
price = 999.9912
print(f"Item: {item} | Price: ${price:.2f}") # Output: Item: Laptop | Price: $999.99
```

---

## 💡 Best Practices
1. Use **snake_case** for variable and function names (`user_age`, `total_amount`).
2. Keep variables descriptive (`student_name` instead of `sn`).
3. Always remember `input()` returns a string; cast it if numerical calculations are required!
