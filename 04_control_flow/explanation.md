# 04. Decision Making & Control Flow in Python

## 📌 Overview
Control flow statements determine the order in which code executes based on conditions and loops.

---

## 🔑 Key Concepts

### 1. Decision Making (`if`, `elif`, `else`)
Executes code blocks based on truth values.
```python
if condition1:
    # Code block 1
elif condition2:
    # Code block 2
else:
    # Default fallback block
```

### 2. Ternary Operator (Conditional Expression)
Single-line syntax: `value_if_true if condition else value_if_false`
```python
status = "Adult" if age >= 18 else "Minor"
```

### 3. Loop Structures (`for` & `while`)
- **`for` loop**: Iterates over a sequence (`range()`, `list`, `str`, `tuple`, `dict`).
- **`range(start, stop[, step])`**: Generates arithmetic progression (excludes `stop`).
- **`while` loop**: Repeats as long as condition evaluates to `True`.

### 4. Loop Control Statements
- `break`: Terminates loop immediately.
- `continue`: Skips remainder of current iteration and moves to next.
- `pass`: Null statement (placeholder).

### 5. `for-else` & `while-else` Constructs
The `else` block after a loop executes **only if the loop completed normally** (i.e. without encountering a `break` statement).
```python
for i in range(2, 10):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("Prime number!") # Executes only if loop completes without break
```
