# ❓ 05. String Manipulation - Questions & Exercises

## 📝 Conceptual Questions

### Q1: Why are strings immutable in Python?
**Answer:** Immutability provides thread safety, security (e.g., when used as dict keys or database credentials), and allows Python to optimize memory via string interning.

### Q2: What is the difference between `str.find()` and `str.index()`?
**Answer:**
- `find(sub)` returns `-1` if the substring `sub` is not found.
- `index(sub)` raises a `ValueError` exception if the substring `sub` is not found.

---

## 💻 Practical Exercises & Solutions

### Challenge 1: Title Case Converter Without Built-In `.title()`
Convert `"hello world python"` into Title Case (`"Hello World Python"`) using `.split()` and `.capitalize()`.

**Solution:**
```python
text = "hello world python"
title_cased = " ".join(word.capitalize() for word in text.split())
print("Title Case:", title_cased)
```

### Challenge 2: Anagram Verification
Write a condition to check if two strings `"listen"` and `"silent"` are anagrams.

**Solution:**
```python
str1 = "listen"
str2 = "silent"
is_anagram = sorted(str1.lower()) == sorted(str2.lower())
print(f"Are '{str1}' and '{str2}' anagrams? -> {is_anagram}")
```
