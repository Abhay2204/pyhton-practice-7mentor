# ❓ 14. Python Functions - Questions & Coding Challenges

## 📝 Conceptual Questions

### Q1: What is the difference between a parameter and an argument?
**Answer:**
- **Parameter**: The variable listed inside the parentheses in the function definition (e.g., `def add(a, b):`).
- **Argument**: The actual value sent to the function when it is invoked (e.g., `add(10, 20)`).

### Q2: Why is using a mutable default argument (like `def func(lst=[])`) considered an anti-pattern?
**Answer:**
Default arguments are evaluated **once** when the function is defined, not each time the function is called. If you mutate a default list or dict, that mutation persists across subsequent calls. The recommended pattern is:
```python
def func(lst=None):
    if lst is None:
        lst = []
    lst.append(1)
    return lst
```

### Q3: What is the LEGB rule in Python?
**Answer:**
LEGB describes Python's name resolution lookup order:
1. **L**ocal: Inside the current function.
2. **E**nclosing: In any enclosing functions (closures).
3. **G**lobal: Module top-level variables.
4. **B**uilt-in: Python's built-in namespace (`len`, `range`, `print`).

### Q4: How do `*args` and `**kwargs` differ?
**Answer:**
- `*args` collects arbitrary positional arguments into a **tuple**.
- `**kwargs` collects arbitrary keyword arguments into a **dictionary**.

### Q5: What is a Lambda function and when should it be used?
**Answer:**
A `lambda` function is a small anonymous function containing a single expression. It is typically used for short, throwaway operations—such as passing a `key` function to `sorted()`, `min()`, or `max()`, or within `map()` and `filter()`.

---

## 🔍 Tricky Output Questions

### Tricky Q1: Variable Scope & Reassignment
```python
x = 10
def modify():
    x = 20
    print("Inside:", x)

modify()
print("Outside:", x)
```
**Output:**
```
Inside: 20
Outside: 10
```
*Explanation:* `x = 20` inside `modify()` assigns to a local variable `x`, leaving the global `x` untouched.

### Tricky Q2: Default Argument Retention
```python
def append_val(val, target=[]):
    target.append(val)
    return target

print(append_val(1))
print(append_val(2))
```
**Output:**
```
[1]
[1, 2]
```
*Explanation:* The default list `[]` is created once when the function is defined and reused in both calls.

---

## 💻 Coding Exercises & Solutions

### Challenge 1: Variable-Length Sum & Average
**Problem:** Write a function `stats(*numbers)` that takes any count of numbers and returns their count, sum, and average.
```python
def stats(*numbers):
    if not numbers:
        return 0, 0, 0.0
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return count, total, round(avg, 2)

print(stats(10, 20, 30, 40))  # (4, 100, 25.0)
```

### Challenge 2: Prime Number Checker
**Problem:** Write a function `is_prime(n)` that returns `True` if `n` is prime and `False` otherwise.
```python
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

print(is_prime(17))  # True
print(is_prime(24))  # False
```

### Challenge 3: Recursive Fibonacci Generator
**Problem:** Write a recursive function `fibonacci(n)` that returns the n-th Fibonacci number (0-indexed: 0, 1, 1, 2, 3, 5...).
```python
def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Index must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(8)])  # [0, 1, 1, 2, 3, 5, 8, 13]
```

### Challenge 4: Word Frequency Dictionary
**Problem:** Write a function `count_words(sentence)` that normalizes case, removes punctuation, and returns a dictionary with word counts.
```python
import string

def count_words(sentence: str) -> dict:
    cleaned = sentence.lower().translate(str.maketrans("", "", string.punctuation))
    words = cleaned.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

print(count_words("Python is great and Python is versatile!"))
# {'python': 2, 'is': 2, 'great': 1, 'and': 1, 'versatile': 1}
```
