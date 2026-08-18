# ❓ 12. Python `for` Loops - Questions & Challenges

## 📝 Conceptual Questions

### Q1: How does a Python `for` loop differ from traditional `for` loops in C/C++ or Java?
**Answer:** In C/C++ or Java, `for` loops are index/condition-based (`for (int i=0; i<n; i++)`). In Python, a `for` loop is an **iterator-based loop (foreach)** that directly traverses elements of an iterable sequence without requiring manual index manipulation.

### Q2: What is the purpose of `enumerate()`?
**Answer:** `enumerate()` yields a tuple `(index, item)` during each iteration, allowing you to track index positions cleanly without creating an external counter variable.

### Q3: When does the `else` clause attached to a `for` loop run?
**Answer:** It executes **only when the loop completes all iterations naturally** without hitting a `break` statement.

---

## 💻 Coding Exercises & Solutions

### Challenge 1: Multiplication Table
**Problem:** Generate the multiplication table for a given integer up to 10.
```python
num = 6
for i in range(1, 11):
    print(f"{num} x {i:2d} = {num * i}")
```

### Challenge 2: Count Vowels and Consonants in a String
**Problem:** Count vowels and consonants in `"Python Programming"`.
```python
text = "Python Programming".lower()
vowels = 0
consonants = 0

for char in text:
    if char.isalpha():
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1

print(f"Vowels: {vowels}, Consonants: {consonants}")
```

### Challenge 3: Inverted Triangle Star Pattern
**Problem:** Print an inverted star triangle of 5 rows.
```python
rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
```

### Challenge 4: Sum of Digits of a Number
**Problem:** Calculate the sum of digits of `9876` using a `for` loop.
```python
num_str = "9876"
digit_sum = 0
for digit in num_str:
    digit_sum += int(digit)
print(f"Sum of digits: {digit_sum}")  # 30
```

---

### Challenge 5: Multiplication Table of 124 with Even/Odd Label
**Problem:** Print the multiplication table of `124` from 1 to 10 using a `for` loop.
For each result, use an `if/else` to label whether the product is **Even** or **Odd**.

**Expected Output:**
```
124 x  1 =   124  → Even
124 x  2 =   248  → Even
124 x  3 =   372  → Even
...
124 x 10 =  1240  → Even
```

**Solution — Approach 1: `for` loop + `if/else`**
```python
number = 124

print(f"--- Multiplication Table of {number} ---")
for i in range(1, 11):
    result = number * i
    if result % 2 == 0:
        label = "Even"
    else:
        label = "Odd"
    print(f"{number} x {i:2d} = {result:5d}  → {label}")
```

**Solution — Approach 2: Ternary (one-liner `if/else`)**
```python
number = 124

print(f"--- Multiplication Table of {number} (Ternary) ---")
for i in range(1, 11):
    result = number * i
    label = "Even" if result % 2 == 0 else "Odd"
    print(f"{number} x {i:2d} = {result:5d}  → {label}")
```

> 💡 **Observation:** Since 124 is even, multiplying it by any integer always gives an **Even** result.
> The `if/else` check is still good practice — try it with an odd number like `125` to see `Odd` labels appear!
