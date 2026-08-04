# ❓ 09. Dictionaries - Questions & Exercises

## 📝 Conceptual Questions

### Q1: What makes a type valid as a dictionary key in Python?
**Answer:** A object must be **hashable** (its hash value never changes during its lifetime). Immutable types (`str`, `int`, `float`, `tuple`, `frozenset`) are valid keys. Mutable types (`list`, `dict`, `set`) raise `TypeError: unhashable type`.

### Q2: How do you merge two dictionaries `d1` and `d2` in Python 3.9+?
**Answer:** Using the union operator `|`: `merged = d1 | d2` or in-place `d1 |= d2`.

---

## 💻 Practical Exercises & Solutions

### Challenge 1: Invert Dictionary (Keys <-> Values)
Invert dictionary `{"a": 1, "b": 2, "c": 3}` into `{1: "a", 2: "b", 3: "c"}`.

**Solution:**
```python
d = {"a": 1, "b": 2, "c": 3}
inverted = {v: k for k, v in d.items()}
print("Inverted Dict:", inverted)
```

### Challenge 2: Group Words by Length
Group words `["cat", "dog", "apple", "banana", "bat"]` by word length.

**Solution:**
```python
words = ["cat", "dog", "apple", "banana", "bat"]
grouped = {}
for word in words:
    length = len(word)
    grouped.setdefault(length, []).append(word)

print("Grouped by length:", grouped) # {3: ['cat', 'dog', 'bat'], 5: ['apple'], 6: ['banana']}
```
