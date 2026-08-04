# ❓ 02. Typecasting & Coercion - Questions & Exercises

## 📝 Conceptual Questions

### Q1: Why does `int("12.34")` throw an error, while `float("12.34")` works?
**Answer:** `int()` expects a valid base-10 integer string (digits only). When given a string with a decimal point `.` it raises `ValueError`. To convert `"12.34"` to `int`, cast to `float` first: `int(float("12.34"))`.

### Q2: What are "Falsy" values in Python?
**Answer:** In Python, the following evaluate to `False` under `bool()`:
- `0`, `0.0`, `0j`
- `""` (empty string)
- `[]` (empty list)
- `()` (empty tuple)
- `{}` (empty dict)
- `set()` (empty set)
- `None`
- `False`

---

## 💻 Practical Exercises & Solutions

### Challenge 1: Clean Price String
Extract float value from currency string `"$149.99"` and calculate total for 3 units.

**Solution:**
```python
price_input = "$149.99"
qty = 3
clean_price = float(price_input.replace("$", ""))
total = clean_price * qty
print(f"Total: ${total:.2f}")
```

### Challenge 2: Hexadecimal to Integer Conversion
Convert hex string `"FF"` to integer.

**Solution:**
```python
hex_val = "FF"
dec_val = int(hex_val, 16)
print("Decimal equivalent:", dec_val) # 255
```
