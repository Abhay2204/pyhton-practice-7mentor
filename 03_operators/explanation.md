# 03. Operators in Python

## 📌 Overview
Operators are special symbols used to perform computations on variables and values (operands).

---

## 🔑 Key Operator Categories

### 1. Arithmetic Operators
- `+` (Addition), `-` (Subtraction), `*` (Multiplication), `/` (Float Division)
- `//` (Floor Division — truncates fractional part), `%` (Modulus — remainder), `**` (Exponentiation)

### 2. Relational / Comparison Operators
- `==` (Equal), `!=` (Not Equal), `>` (Greater than), `<` (Less than), `>=` (Greater or equal), `<=` (Less or equal)
- Python supports **chained comparisons**: `10 <= x <= 20`.

### 3. Logical Operators (Short-Circuit Evaluation)
- `and`: Returns `True` if both operands are `True`.
- `or`: Returns `True` if at least one operand is `True`.
- `not`: Inverts the boolean value.

### 4. Identity Operators (`is` vs `==`)
- `is`: Checks if two variables point to the **exact same memory location** (`id(a) == id(b)`).
- `==`: Checks if two variables have **equal values**.

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b) # True (Same values)
print(a is b) # False (Different memory addresses)
```

### 5. Membership Operators (`in`, `not in`)
- Checks if a sequence contains a specified element (works on `str`, `list`, `tuple`, `set`, `dict`).
- For dictionaries, `in` checks **keys** by default. Use `.values()` to check values.

### 6. Bitwise Operators
- `&` (AND), `|` (OR), `^` (XOR), `~` (NOT / 2's complement), `<<` (Left Shift), `>>` (Right Shift).

---

## 🔝 Operator Precedence (Highest to Lowest)
1. `()` Parentheses
2. `**` Exponentiation
3. `+x`, `-x`, `~x` Unary positive/negative/bitwise NOT
4. `*`, `/`, `//`, `%` Multiplication, Division, Floor div, Modulus
5. `+`, `-` Addition, Subtraction
6. `<<`, `>>` Bitwise Shifts
7. `&` Bitwise AND
8. `^` Bitwise XOR
9. `|` Bitwise OR
10. `==`, `!=`, `>`, `>=`, `<`, `<=`, `is`, `is not`, `in`, `not in` Comparisons & Identity/Membership
11. `not` Logical NOT
12. `and` Logical AND
13. `or` Logical OR
14. `=`, `+=`, `-=`, `*=`, etc. Assignments
