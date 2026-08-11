# 🔄 12. Python `for` Loops Mastery & Practice

Welcome to the comprehensive module on **`for` Loops in Python** as part of the 7Mentor Python curriculum.

---

## 📑 Table of Contents
- [1. Overview & Conceptual Understanding](#1-overview--conceptual-understanding)
- [2. Syntax & Mechanics](#2-syntax--mechanics)
- [3. Deep Dive into `range()`](#3-deep-dive-into-range)
- [4. Iteration Across Python Data Structures](#4-iteration-across-python-data-structures)
- [5. Essential Loop Built-ins (`enumerate`, `zip`, `reversed`)](#5-essential-loop-built-ins)
- [6. Loop Control Statements (`break`, `continue`, `pass`)](#6-loop-control-statements)
- [7. The `for...else` Construct](#7-the-forelse-construct)
- [8. Nested Loops & Pattern Printing](#8-nested-loops--pattern-printing)
- [9. Real-World Applications & Algorithms](#9-real-world-applications--algorithms)
- [10. Exercises & Practice Questions](#10-exercises--practice-questions)

---

## 1. Overview & Conceptual Understanding

In Python, a `for` loop is a **definite iteration** statement that steps through items of any iterable (such as sequences like `str`, `list`, `tuple`, or collections like `dict`, `set`, and generators like `range()`).

```
                +-------------------------+
                |     Iterable Sequence    |
                |  ['Apple', 'Banana', 'Mango'] |
                +-------------------------+
                             |
                   Fetch next element
                             v
               +---------------------------+
  +----------> | Element exists?           |
  |            +---------------------------+
  |                   /             \
  |             YES  /               \  NO (Exhausted)
  |                 v                 v
  |      +--------------------+     +-------------------+
  |      | Assign to variable |     | Loop Terminates   |
  |      | Execute loop body  |     | (or executes else)|
  |      +--------------------+     +-------------------+
  |                 |
  +-----------------+
```

---

## 2. Syntax & Mechanics

### Standard Syntax
```python
for item in iterable:
    # Loop body: executed once per item
    print(item)
```

- **`item`**: A target variable that automatically stores the current element for that iteration.
- **`iterable`**: Any Python object capable of returning its members one at a time.

---

## 3. Deep Dive into `range()`

The `range(start, stop, step)` built-in produces an immutable sequence of integers.

| Variation | Syntax | Output Sequence | Notes |
| :--- | :--- | :--- | :--- |
| **1 Argument** | `range(5)` | `0, 1, 2, 3, 4` | Defaults `start=0`, `step=1`. Excludes `stop` (5). |
| **2 Arguments** | `range(2, 7)` | `2, 3, 4, 5, 6` | Starts at `2`, ends before `7`. |
| **3 Arguments (Positive Step)** | `range(1, 10, 2)` | `1, 3, 5, 7, 9` | Skips by `+2`. |
| **3 Arguments (Negative Step)** | `range(10, 0, -2)` | `10, 8, 6, 4, 2` | Countdown decrementing by `-2`. |

### Code Demonstration:
```python
# 1. Forward range
for i in range(1, 6):
    print(i, end=" ")  # 1 2 3 4 5
print()

# 2. Reverse countdown
for i in range(5, 0, -1):
    print(i, end=" ")  # 5 4 3 2 1
print()
```

---

## 4. Iteration Across Python Data Structures

### A. Strings
```python
message = "PYTHON"
for char in message:
    print(char, end=" ")
# Output: P Y T H O N
```

### B. Lists & Tuples
```python
fruits = ["Apple", "Mango", "Cherry"]
for fruit in fruits:
    print(f"Fruit: {fruit}")
```

### C. Dictionaries
```python
student = {"name": "Abhay", "roll": 101, "course": "Python"}

# 1. Iterating keys
for key in student:
    print(key, "->", student[key])

# 2. Iterating key-value pairs directly with .items()
for key, value in student.items():
    print(f"{key.capitalize()}: {value}")
```

### D. Sets
```python
unique_numbers = {10, 20, 30, 40}
for num in unique_numbers:
    print(num)
```

---

## 5. Essential Loop Built-ins

### 🔹 `enumerate()` — Tracking Loop Index
Avoid manually managing counter variables:
```python
languages = ["Python", "Java", "C++", "JavaScript"]

for index, lang in enumerate(languages, start=1):
    print(f"{index}. {lang}")
```

### 🔹 `zip()` — Parallel Iteration Over Multiple Lists
```python
students = ["Abhay", "Rohit", "Sneha"]
marks = [95, 88, 92]

for name, score in zip(students, marks):
    print(f"{name} scored {score}%")
```

### 🔹 `reversed()` & `sorted()`
```python
nums = [4, 1, 9, 3]

for n in sorted(nums):
    print(n, end=" ")  # 1 3 4 9
print()

for n in reversed(nums):
    print(n, end=" ")  # 3 9 1 4
print()
```

---

## 6. Loop Control Statements

```
  +-------------+       +---------------+       +------------+
  |    break    |       |   continue    |       |    pass    |
  +-------------+       +---------------+       +------------+
  Immediately stops     Skips current step      Placeholder;
  and exits loop        jumps to next item      does nothing
```

```python
# 'break' example
for num in range(1, 10):
    if num == 5:
        break
    print(num, end=" ")  # Output: 1 2 3 4
print()

# 'continue' example
for num in range(1, 6):
    if num == 3:
        continue
    print(num, end=" ")  # Output: 1 2 4 5
print()
```

---

## 7. The `for...else` Construct

In Python, the `else` block tied to a `for` loop runs **only when the loop completes all iterations without hitting a `break`**.

```python
target = 17
numbers = [2, 4, 6, 8, 10]

for n in numbers:
    if n == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} was NOT present in the list.")
```

---

## 8. Nested Loops & Pattern Printing

```python
# 1. Right-angled Star Triangle
rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# 2. Number Pyramid
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

---

## 9. Real-World Applications & Algorithms

### A. Multiplication Table Generator
```python
num = 7
print(f"--- Multiplication Table of {num} ---")
for i in range(1, 11):
    print(f"{num} x {i:2d} = {num * i}")
```

### B. Factorial Calculation
```python
n = 5
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial of {n} is: {fact}")  # 120
```

### C. Prime Number Checker
```python
num = 29
if num < 2:
    print(f"{num} is not prime.")
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            print(f"{num} is composite (divisible by {i}).")
            break
    else:
        print(f"{num} is a PRIME number!")
```

---

## 10. Exercises & Practice Questions

Check out the companion files in this directory:
- 📖 [`explanation.md`](explanation.md): Complete theoretical breakdown.
- 🐍 [`examples.py`](examples.py): Working code examples.
- ❓ [`questions.md`](questions.md): 10+ Interview & assignment challenges.
- 💻 [`practice.py`](practice.py): Interactive practice script.
