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
