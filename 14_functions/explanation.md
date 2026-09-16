# 14. Python Functions: Modular & Reusable Programming

## 📌 Overview
A **function** is a self-contained block of organized, reusable code designed to perform a single, related action. In Python, functions are **first-class citizens**—they can be assigned to variables, stored in data structures, passed as arguments to other functions, and returned from functions.

---

## 🔑 Key Concepts

### 1. Function Anatomy & Definition
Functions are defined using the `def` keyword followed by the function name, parentheses `()`, and a colon `:`.

```python
def greet(name: str) -> str:
    """Return a personalized greeting message."""
    return f"Hello, {name}!"
```

- **`def`**: Keyword declaring a function definition.
- **Function Name**: Descriptive snake_case identifier.
- **Parameters**: Variables listed inside parentheses in the function definition.
- **Arguments**: Actual values passed into the function upon invocation.
- **Docstring (`"""..."""`)**: Documents purpose, parameters, and return types (accessible via `help()` and `__doc__`).
- **`return`**: Terminates function execution and sends values back to the caller. Without an explicit `return`, Python implicitly returns `None`.

---

### 2. Parameters vs Arguments

Python offers versatile parameter passing modes:

| Parameter Type | Syntax Example | Notes |
| :--- | :--- | :--- |
| **Positional** | `def add(a, b):` | Arguments are mapped strictly by position. |
| **Keyword** | `add(b=10, a=5)` | Arguments are explicitly named, order does not matter. |
| **Default** | `def connect(port=8080):` | Provides a fallback value if omitted during invocation. |
| **Positional-Only** | `def f(a, b, /):` | Arguments before `/` cannot be passed by keyword (Python 3.8+). |
| **Keyword-Only** | `def f(*, key):` | Arguments after `*` must be passed by keyword. |

> [!WARNING]
> **Mutable Default Arguments Trap**: Never use mutable objects (like lists or dictionaries) as default argument values (e.g., `def append_to(item, target=[])`). The default is evaluated once at definition time, sharing the same object across all calls. Instead, use `target=None` and initialize inside the function.

---

### 3. Variable-Length Arguments (`*args` & `**kwargs`)

- **`*args` (Tuple Unpacking)**: Collects any arbitrary number of positional arguments into a tuple.
- **`**kwargs` (Dictionary Unpacking)**: Collects any arbitrary number of keyword arguments into a dictionary.

```python
def make_profile(username, *skills, **metadata):
    print(f"User: {username}")
    print(f"Skills (tuple): {skills}")
    print(f"Metadata (dict): {metadata}")

make_profile("abhay", "Python", "SQL", "Git", role="Developer", city="Pune")
```

---

### 4. Scope & The LEGB Rule

Python resolves variable names following the **LEGB hierarchy**:

1. **L — Local**: Names assigned inside a function (not declared `global`).
2. **E — Enclosing**: Names in the local scope of enclosing functions (closures / nested functions).
3. **G — Global**: Names declared at the top-level of a module or explicitly marked `global`.
4. **B — Built-in**: Names preloaded into Python (e.g., `print`, `range`, `len`).

#### Scope Modifiers:
- **`global var_name`**: Tells Python to rebind a top-level module variable from inside a function.
- **`nonlocal var_name`**: Tells Python to rebind a variable from the nearest enclosing (outer) function.

---

### 5. Lambda (Anonymous) Functions
Short, single-expression inline functions created using the `lambda` keyword:

```python
# Syntax: lambda arg1, arg2, ...: expression
square = lambda x: x ** 2
multiply = lambda a, b: a * b
```

Best used with higher-order functions:
- **`map(func, iterable)`**: Applies `func` to every item in the iterable.
- **`filter(func, iterable)`**: Keeps items where `func(item)` evaluates to `True`.
- **`sorted(iterable, key=func)`**: Sorts items based on custom criteria.

---

### 6. Recursion & Base Condition
A function that calls itself to solve a smaller instance of the same problem. Every recursive function **must** have:
1. **Base Case**: Halting condition that returns without recursing.
2. **Recursive Step**: Moves progressively closer to the base case.

```python
def factorial(n: int) -> int:
    if n <= 1:           # Base case
        return 1
    return n * factorial(n - 1)  # Recursive step
```

---

### 7. Modular Design & Code Organization
- Break complex problems down into small, single-responsibility functions.
- Separate logic (computation/business rules) from user interface (terminal input/output).
- Organize utility functions into separate Python files (modules) and import them cleanly using `from module import func`.
