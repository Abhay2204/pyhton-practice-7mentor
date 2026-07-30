# 🐍 Python 7Mentor Mastery & Practice Tracker

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Progress](https://img.shields.io/badge/Progress-100%25%20Completed-brightgreen.svg?style=for-the-badge&logo=checkmark)
![Modules](https://img.shields.io/badge/Modules-9%20Files-orange.svg?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-purple.svg?style=for-the-badge)

<p align="center">
  <b>A comprehensive, production-grade Python practice repository tracking core concepts, data structures, control flows, and real-world scenario implementations from 7Mentor training.</b>
</p>

[📌 Core Modules](#-curriculum--progress-tracker) •
[🚀 Quick Start](#-quick-start--usage) •
[📊 Topic Deep Dives](#-topic-deep-dives--code-highlights) •
[💡 Real-World Demos](#-real-world-mini-projects)

</div>

---

## 📈 Learning Progress Dashboard

```
Overall Syllabus Completion: [████████████████████████████████] 100%
```

| Module / Topic | File | Concepts Covered | Status |
| :--- | :--- | :--- | :---: |
| **01. Fundamentals & Operators** | [`basics_practice.py`](basics_practice.py) | Variables, Types, Casting, F-Strings, Arithmetic, Comparison & Logical Operators | `![Completed](https://img.shields.io/badge/-DONE-brightgreen)` |
| **02. Decision Making & Loops** | [`control_flow_practice.py`](control_flow_practice.py) | `if/elif/else`, Leap Year (3 methods), Ternary, `range()`, `while`, Loop Control (`break`/`continue`), `for-else` | `![Completed](https://img.shields.io/badge/-DONE-brightgreen)` |
| **03. String Manipulation** | [`string_practice.py`](string_practice.py) | Indexing, Slicing, Case Methods, Search/Count, Strip, Split/Join, Formatting, Palindrome & Vowels | `![Completed](https://img.shields.io/badge/-DONE-brightgreen)` |
| **04. Lists & Operations** | [`list_practice.py`](list_practice.py) | Indexing, Slicing, `.append()`, `.insert()`, `.extend()`, `.pop()`, `.remove()`, `.sort()`, Aggregations | `![Completed](https://img.shields.io/badge/-DONE-brightgreen)` |
| **05. Tuples & Immutability** | [`tuple_practice.py`](tuple_practice.py) | Single-element Tuples, Slicing, Immutability workarounds, Packing & Extended Unpacking (`*tail`), Nested Tuples | `![Completed](https://img.shields.io/badge/-DONE-brightgreen)` |
| **06. Set Theory & Operations** | [`set_practice.py`](set_practice.py) | Uniqueness, `.add()`, `.update()`, `.remove()` vs `.discard()`, Union (`\|`), Intersect (`&`), Diff (`-`), Sym-Diff (`^`), Frozenset | `![Completed](https://img.shields.io/badge/-DONE-brightgreen)` |
| **07. Dictionaries & Collections** | [`dict_practice.py`](dict_practice.py) | Key-Value Access, `.get()`, Key/Value Iteration (`.items()`), Word Frequency Counter, Deduplication | `![Completed](https://img.shields.io/badge/-DONE-brightgreen)` |
| **08. Real World: Inventory** | [`newspaper_seller.py`](newspaper_seller.py) | List `.copy()`, element removal, and state isolation in a newspaper vendor workflow | `![Completed](https://img.shields.io/badge/-DONE-brightgreen)` |
| **09. Real World: Management** | [`ssmv_school.py`](ssmv_school.py) | Set range generation, sequence sorting, and dynamic roll number management | `![Completed](https://img.shields.io/badge/-DONE-brightgreen)` |

---

## 📁 Repository Architecture

```tree
pyhton practice 7mentor/
├── 📜 README.md                    # Detailed progress tracking & document hub
├── 🐍 basics_practice.py           # Variables, casting, I/O, operators
├── 🐍 control_flow_practice.py     # Decision logic, loops, leap year logic
├── 🐍 string_practice.py          # String indexing, slicing, methods, & algorithms
├── 🐍 list_practice.py            # Comprehensive list CRUD, sorting & filters
├── 🐍 tuple_practice.py           # Immutability, unpacking & nested tuple operations
├── 🐍 set_practice.py             # Mathematical sets, venn logic & frozensets
├── 🐍 dict_practice.py            # Dictionary manipulation & word counting
├── 🐍 newspaper_seller.py         # Real-world list copy & basket simulation
└── 🐍 ssmv_school.py              # Real-world roll number tracking with sets
```

---

## 🎯 Topic Deep Dives & Code Highlights

### 1️⃣ Fundamentals & Operators (`basics_practice.py`)
- **Key Concepts**: Dynamic typing, type casting (`str` to `int`, float truncation, boolean truthiness), string interpolation with `f-strings`.
- **Operators**: Addition, floor division (`//`), exponentiation (`**`), modulus (`%`), short-circuit logical operators (`and`, `or`, `not`).

```python
# F-string Formatting Example
product, price, quantity = "Laptop", 899.99, 2
print(f"Product: {product}\nTotal Cost: ${price * quantity:.2f}")
```

---

### 2️⃣ Control Flow & Logic (`control_flow_practice.py`)
- **Key Concepts**: Grade assignment, ternary operators, `range()` stepping & countdowns, `enumerate()`, `while` loop factorials.
- **Featured Implementation**: **3 Approaches to Leap Year Calculation**:
  1. `calendar.isleap(year)` — Standard library module.
  2. `if/elif/else` cascade — Explicit logical breakdown.
  3. `(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)` — Single-line boolean condition.
- **For-Else Loop**: Demonstrates prime number evaluation where the `else` block executes only if no `break` occurred.

---

### 3️⃣ String Engineering (`string_practice.py`)
- **Key Concepts**: Slicing step syntax (`[::-1]` for string reversal), case transformations (`upper()`, `title()`, `swapcase()`), cleaning (`strip()`), search (`find()`, `startswith()`, `endswith()`).
- **Challenges**:
  - **Vowel Counter**: Iterating through text to identify vowel frequencies.
  - **Palindrome Verification**: Comparing string with its reverse slice.

---

### 4️⃣ List Mastery (`list_practice.py`)
- **Key Concepts**: Indexing & negative indexing, sub-slicing, list mutation (`append`, `insert`, `extend`), element removal (`remove`, `pop`, `del`, `clear`), sorting (`sort(reverse=True)`), aggregations (`sum`, `min`, `max`, `len`).
- **Filtering**: Extracting even numbers via step slicing (`mix_numbers[1::2]`) and set deduplication.

---

### 5️⃣ Tuples & Immutability (`tuple_practice.py`)
- **Key Concepts**: Immutable sequences, single-element tuple syntax `("python",)`, list-casting workarounds for tuple modification, packing and unpacking.
- **Extended Unpacking**:
  ```python
  data = (100, 200, 300, 400, 500)
  head, *tail = data
  # head -> 100, tail -> [200, 300, 400, 500]
  ```

---

### 6️⃣ Set Theory & Venn Logic (`set_practice.py`)
- **Key Concepts**: Unique elements, set creation vs empty dict `{}` pitfall, error-safe removal (`discard` vs `remove`).
- **Venn Math Operations**:
  - **Union** (`|` or `.union()`)
  - **Intersection** (`&` or `.intersection()`)
  - **Difference** (`-` or `.difference()`)
  - **Symmetric Difference** (`^` or `.symmetric_difference()`)
  - **Immutable Sets**: `frozenset([10, 20, 30])`

---

### 7️⃣ Dictionaries & Frequency Analysis (`dict_practice.py`)
- **Key Concepts**: Key-value lookup, safe retrieval via `.get()`, dictionary mutations, `.keys()`, `.values()`, `.items()` loops.
- **Practical Application**: Word frequency counter algorithm utilizing dict key accumulation.

---

## 💡 Real-World Mini Projects

### 📰 Newspaper Vendor & IAS Basket Simulation (`newspaper_seller.py`)
Demonstrates independent list object cloning using `.copy()` to isolate inventory changes between a vendor stock and a customer's basket.
```python
newspaper = ["Times of India", "Hindustan Times", "Dainik Bhaskar", "The Indian Express", "Navbharat Times"]
ias_basket = newspaper.copy()
ias_basket.remove("Times of India")
```

### 🏫 SSMV School Roll Number Tracking (`ssmv_school.py`)
Utilizes Python `set` and `range()` to model roll number assignments from 1 to 60 and dynamically reflect student drops.
```python
school_rolls = set(range(1, 61))
school_rolls.remove(35) # Roll 35 removed
```

---

## 🚀 Quick Start & Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Abhay2204/pyhton-practice-7mentor.git
   cd "pyhton practice 7mentor"
   ```

2. **Run Any Practice Script**:
   ```bash
   # Basics & Operators
   python basics_practice.py

   # Control Flow & Leap Year
   python control_flow_practice.py

   # Data Structures
   python string_practice.py
   python list_practice.py
   python tuple_practice.py
   python set_practice.py
   python dict_practice.py

   # Mini Projects
   python newspaper_seller.py
   python ssmv_school.py
   ```

---

## ✅ Skills & Concept Tracking Checklist

- [x] Variable declaration & dynamic typing
- [x] Type casting (`int()`, `float()`, `str()`, `bool()`)
- [x] F-strings & numerical formatting
- [x] Arithmetic, comparison & logical operators
- [x] Conditional branches (`if`, `elif`, `else`)
- [x] Leap year calculation (3 methods)
- [x] Ternary operators
- [x] `for` loops, `range()` & `enumerate()`
- [x] `while` loops & factorials
- [x] `break`, `continue`, `pass` & `for-else` prime checks
- [x] String slicing, reversing & immutability
- [x] String methods (`upper`, `lower`, `title`, `strip`, `split`, `join`)
- [x] List CRUD & in-place sorting
- [x] List comprehensions & deduplication
- [x] Tuple creation, packing & extended unpacking (`*tail`)
- [x] Mathematical Set operations (`|`, `&`, `-`, `^`)
- [x] Safe element removal (`discard` vs `remove`)
- [x] Immutable `frozenset` usage
- [x] Dictionary operations, `.get()`, & key-value iteration
- [x] Frequency counter algorithms

---

<div align="center">
  <sub>Maintained with ❤️ by <b>Abhay Mallick</b> as part of Python Training at 7Mentor.</sub>
</div>
