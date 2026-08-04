# ❓ 03. Python Operators - Questions & Exercises

## 📝 Conceptual Questions

### Q1: What is the result of `10 + 2 * 3 ** 2 - 8 // 4` and why?
**Answer:**
1. Exponentiation `3 ** 2` = `9`
2. Multiplication `2 * 9` = `18`
3. Floor Division `8 // 4` = `2`
4. Addition `10 + 18` = `28`
5. Subtraction `28 - 2` = **`26`**

### Q2: What is the bitwise NOT `~` formula in Python?
**Answer:** `~x` is calculated as `-(x + 1)`. Therefore `~12` evaluates to `-13`.

### Q3: How does Python evaluate `a and b` when `a` is Falsy?
**Answer:** Due to short-circuiting, if `a` is Falsy, Python immediately returns `a` without evaluating `b`.

---

## 💻 Practical Exercises & Solutions

### Challenge 1: Bitwise Swap
Swap two numbers `x = 10` and `y = 20` using Bitwise XOR (`^`) without a temporary variable.

**Solution:**
```python
x = 10
y = 20

x = x ^ y
y = x ^ y
x = x ^ y

print(f"Swapped: x = {x}, y = {y}") # x = 20, y = 10
```

### Challenge 2: E-Commerce Discount & Shipping Calculator
Calculate final price for item cost `$100`, qty `3`, 10% discount if subtotal > 200, flat $15 shipping if net < 250 else $0.

**Solution:**
```python
price = 100
qty = 3
subtotal = price * qty
discount = (subtotal * 0.10) if subtotal > 200 else 0
after_discount = subtotal - discount
shipping = 0 if after_discount >= 250 else 15
final_payable = after_discount + shipping

print(f"Final Payable: ${final_payable:.2f}")
```
