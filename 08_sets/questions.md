# ❓ 08. Set Theory & Operations - Questions & Exercises

## 📝 Conceptual Questions

### Q1: What is the main structural difference between `remove()` and `discard()` on a set?
**Answer:**
- `remove(x)` removes element `x`, but raises `KeyError` if `x` is not present in the set.
- `discard(x)` removes element `x` if present, but does **nothing (no error)** if `x` is absent.

### Q2: Why cannot a regular set be used as a key in a Python dictionary?
**Answer:** A regular set is mutable, meaning its hash value could change if elements are added/removed. Dictionary keys must be hashable and immutable. Use `frozenset` instead.

---

## 💻 Practical Exercises & Solutions

### Challenge 1: Find Common Enrolled Students
Find students enrolled in both Math `{"Alice", "Bob", "Charlie"}` and Physics `{"Bob", "David", "Charlie"}`.

**Solution:**
```python
math = {"Alice", "Bob", "Charlie"}
physics = {"Bob", "David", "Charlie"}
both = math & physics
print("Enrolled in both:", both) # {'Bob', 'Charlie'}
```

### Challenge 2: Unique Word Counter
Count the total number of unique words in a string `"apple banana apple orange banana grape"`.

**Solution:**
```python
text = "apple banana apple orange banana grape"
unique_words = set(text.split())
print("Total unique words:", len(unique_words)) # 4
```
