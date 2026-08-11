# 12. Python `for` Loops & Iteration Mechanics

## 📌 Overview
A `for` loop in Python provides an elegant mechanism for **definite iteration** over sequences (strings, lists, tuples, ranges) and other iterables (dictionaries, sets, generators).

---

## 🔑 Key Concepts

### 1. The `for...in` Statement
Unlike C/Java counter-based loops, Python iterates directly over elements in an iterable.
```python
for item in iterable:
    # process item
```

### 2. `range()` Progression Generator
`range([start], stop, [step])` generates integers lazily on demand:
- **`start`**: Initial value (default `0`).
- **`stop`**: Upper/lower bound (exclusive).
- **`step`**: Increment or decrement value (default `1`).

### 3. Collection Iteration Mechanics
- **Strings**: Yields one character per iteration.
- **Lists / Tuples**: Yields each element in index order.
- **Dictionaries**: Yields keys by default. Use `.values()` for values or `.items()` for key-value tuples.
- **Sets**: Yields elements in arbitrary (hash) order without duplicates.

### 4. Advanced Iteration Tools
- **`enumerate(iterable, start=0)`**: Returns `(index, value)` pairs.
- **`zip(*iterables)`**: Pairs elements from multiple iterables simultaneously until the shortest iterable ends.
- **`reversed(sequence)`**: Iterates over a sequence in reverse without modifying the original object.
- **`sorted(iterable)`**: Iterates through elements in sorted order.

### 5. Loop Control Statements
- **`break`**: Immediately terminates the innermost loop.
- **`continue`**: Skips the remainder of the current iteration body and jumps to the next cycle.
- **`pass`**: Syntactic placeholder doing nothing.

### 6. The `for...else` Construct
The `else` clause executes **only when the loop completes all iterations normally** without encountering a `break` statement.
```python
for item in collection:
    if condition(item):
        break
else:
    # Executes only if break was never reached
    print("Item not found")
```
