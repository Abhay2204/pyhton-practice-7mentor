# ❓ 01. Python Basics & Fundamentals - Questions & Exercises

## 📝 Conceptual Questions

### Q1: What is Dynamic Typing in Python?
**Answer:** Dynamic typing means you do not need to explicitly declare variable types. Python determines a variable's data type at runtime based on the value assigned to it.

### Q2: What is the default return data type of Python's `input()` function?
**Answer:** The `input()` function always returns a string (`str`), even if the user types digits like `123`.

### Q3: What is the difference between single, double, and triple quotes for strings?
**Answer:** Single (`'...'`) and double (`"..."`) quotes are functionally identical for single-line strings. Triple quotes (`'''...'''` or `"""..."""`) allow multi-line strings and docstrings.

---

## 💻 Practical Coding Exercises

### Challenge 1: Bill Splitter
Write a program that takes total bill amount, tip percentage, and number of people, then outputs each person's share formatted to 2 decimal places.

**Solution:**
```python
total_bill = 120.50
tip_percent = 15
people = 4

total_with_tip = total_bill * (1 + tip_percent / 100)
per_person = total_with_tip / people

print(f"Each person pays: ${per_person:.2f}")
```

### Challenge 2: Name & Greeting Generator
Concatenate `first_name` and `last_name` variables and print a formal greeting with upper/lower casing.

**Solution:**
```python
first_name = "ANNURUDH"
last_name = "JADAV"

full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
print(f"Welcome, {full_name}!")
```
