# ❓ 04. Control Flow - Questions & Exercises

## 📝 Conceptual Questions

### Q1: When does the `else` clause in a `for-else` loop execute?
**Answer:** The `else` block executes **only if the loop finishes iterating naturally** through all items, without hitting a `break` statement.

### Q2: What is the difference between `break` and `continue`?
**Answer:**
- `break`: Exits the loop entirely and continues execution after the loop block.
- `continue`: Skips the rest of the current iteration and jumps to the next iteration of the loop.

---

## 💻 Practical Exercises & Solutions

### Challenge 1: Countdown Timer
Write a countdown from `10` down to `1` using `range()` and print `"Blast off!"` at the end.

**Solution:**
```python
for count in range(10, 0, -1):
    print(count, end="... ")
print("Blast off! 🚀")
```

### Challenge 2: Multiples Filter
Print all numbers between 1 and 30 that are divisible by 3 and 5.

**Solution:**
```python
for num in range(1, 31):
    if num % 3 == 0 and num % 5 == 0:
        print(f"Found multiple: {num}") # 15, 30
```
