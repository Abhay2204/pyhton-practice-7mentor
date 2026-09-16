# 🛠️ 14. Python Functions: Modular & Reusable Programming

Welcome to the **Functions Module** of the 7Mentor Python Mastery series. Functions are the cornerstone of clean, testable, and modular software design.

---

## 📑 Module Contents

| File | Type | Description |
| :--- | :---: | :--- |
| [`explanation.md`](explanation.md) | 📖 Guide | In-depth theory: definitions, parameters, `*args`/`**kwargs`, LEGB scope, closures, lambdas, and recursion. |
| [`examples.py`](examples.py) | 💻 Code | Fully runnable code demos illustrating all key concepts. |
| [`questions.md`](questions.md) | ❓ Q&A | Conceptual questions, tricky output predictions, and coding exercises with solutions. |
| [`practice.py`](practice.py) | 🏋️ Practice | Hands-on exercises covering geometry, temperature conversion, variable args, report cards, and recursion. |
| [`process.py`](process.py) | 🧩 Module | Core arithmetic functions (`add`, `sub`, `multiplication`, `division`, `modulus`, `power`). |
| [`newcalculator.py`](newcalculator.py) | 🧮 Project | Terminal calculator demonstrating modular imports and separation of concerns. |

---

## 🔑 Quick Concept Summary

```
                      +-----------------------------+
                      |       def greet(name):      |  <-- Function Signature
                      |         return f"Hi {name}" |  <-- Return Statement
                      +-----------------------------+
                                     ^
                                     | Call with Argument
                      +-----------------------------+
                      |      greet("Abhay")         |
                      +-----------------------------+
```

1. **Parameters vs Arguments**: Parameters are placeholders defined in function signatures; arguments are real values supplied upon calling.
2. **Flexible Signatures**:
   - `*args`: Collects unlimited positional arguments as a `tuple`.
   - `**kwargs`: Collects unlimited keyword arguments as a `dict`.
3. **LEGB Rule**: Resolution order: **L**ocal $\rightarrow$ **E**nclosing $\rightarrow$ **G**lobal $\rightarrow$ **B**uilt-in.
4. **Lambdas**: Compact anonymous functions: `square = lambda x: x ** 2`.
5. **Recursion**: Functions that invoke themselves with base termination conditions.

---

## 🚀 How to Run the Scripts

From the repository root:

```bash
# Run the concept demonstrations
python 14_functions/examples.py

# Run the practice exercises
python 14_functions/practice.py

# Run the modular interactive calculator
python 14_functions/newcalculator.py
```
