# 🐍 Python 7Mentor Mastery & Practice Tracker

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Progress](https://img.shields.io/badge/Progress-In%20Progress-yellow.svg?style=for-the-badge)
![Modules](https://img.shields.io/badge/Topics-12%20Folders-orange.svg?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-purple.svg?style=for-the-badge)

<p align="center">
  <b>A comprehensive, production-grade Python practice repository organized into modular topic folders, each equipped with detailed concept explanations (`explanation.md`), working code demonstrations (`examples.py`), conceptual & coding questions (`questions.md`), and hands-on practice scripts (`practice.py`).</b>
</p>

[📌 Topic Modules](#-learning-progress--topic-modules) •
[📁 Repository Architecture](#-repository-architecture) •
[🔁 While Loop Problems](#-while-loop-problems) •
[🚀 Quick Start](#-quick-start--usage) •
[✅ Skill Checklist](#-skills--concept-tracking-checklist)

</div>

---

## 📈 Learning Progress & Topic Modules

```
Overall Syllabus Completion: [████████████████████████████░░░░] 90%
```

| Topic / Folder | Explanation | Examples | Questions | Practice | Key Concepts Covered |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **[01. Basics & Fundamentals](01_basics/)** | [`explanation.md`](01_basics/explanation.md) | [`examples.py`](01_basics/examples.py) | [`questions.md`](01_basics/questions.md) | [`practice.py`](01_basics/practice.py) | Variables, Types, Dynamic Typing, F-Strings, Input/Output, Concatenation |
| **[02. Typecasting & Coercion](02_typecasting/)** | [`explanation.md`](02_typecasting/explanation.md) | [`examples.py`](02_typecasting/examples.py) | [`questions.md`](02_typecasting/questions.md) | [`practice.py`](02_typecasting/practice.py) | Implicit & Explicit Casting, Collection Conversion, Truthiness, ASCII & Base Conversions |
| **[03. Operator Mastery](03_operators/)** | [`explanation.md`](03_operators/explanation.md) | [`examples.py`](03_operators/examples.py) | [`questions.md`](03_operators/questions.md) | [`practice.py`](03_operators/practice.py) | Arithmetic, Relational, Short-Circuit Logical, Bitwise (`&`/`\|`/`^`/`~`), Identity (`is`), Membership (`in`) |
| **[04. Decision Making & Loops](04_control_flow/)** | [`explanation.md`](04_control_flow/explanation.md) | [`examples.py`](04_control_flow/examples.py) | [`questions.md`](04_control_flow/questions.md) | [`practice.py`](04_control_flow/practice.py) | `if/elif/else`, Leap Year (3 methods), Ternary, `range()`, **`while` loops**, Factorial via `while`, `break`/`continue`, `for-else`, `while-else` |
| **[05. String Engineering](05_strings/)** | [`explanation.md`](05_strings/explanation.md) | [`examples.py`](05_strings/examples.py) | [`questions.md`](05_strings/questions.md) | [`practice.py`](05_strings/practice.py) | Immutability, Step Slicing, Case Methods, Search/Count, Strip, Split/Join, Palindrome & Vowels |
| **[06. Lists & Operations](06_lists/)** | [`explanation.md`](06_lists/explanation.md) | [`examples.py`](06_lists/examples.py) | [`questions.md`](06_lists/questions.md) | [`practice.py`](06_lists/practice.py) | Mutability, CRUD (`append`/`insert`/`extend`/`pop`/`remove`), `.sort()`, List Comprehension, Aggregations |
| **[07. Tuples & Immutability](07_tuples/)** | [`explanation.md`](07_tuples/explanation.md) | [`examples.py`](07_tuples/examples.py) | [`questions.md`](07_tuples/questions.md) | [`practice.py`](07_tuples/practice.py) | Single-element Tuples, Slicing, Immutability Workarounds, Packing & Extended Unpacking (`*tail`), Nested Tuples |
| **[08. Set Theory & Operations](08_sets/)** | [`explanation.md`](08_sets/explanation.md) | [`examples.py`](08_sets/examples.py) | [`questions.md`](08_sets/questions.md) | [`practice.py`](08_sets/practice.py) | Uniqueness, `.add()`, `.update()`, `.remove()` vs `.discard()`, Union (`\|`), Intersect (`&`), Diff (`-`), Sym-Diff (`^`), Frozenset |
| **[09. Dictionaries & Collections](09_dictionaries/)** | [`explanation.md`](09_dictionaries/explanation.md) | [`examples.py`](09_dictionaries/examples.py) | [`questions.md`](09_dictionaries/questions.md) | [`practice.py`](09_dictionaries/practice.py) | Key-Value Access, Safe `.get()`, Key/Value Iteration (`.items()`), Word Frequency Counter, Dict Comprehension |
| **[10. Real World Projects](10_real_world_projects/)** | [`explanation.md`](10_real_world_projects/explanation.md) | [`examples.py`](10_real_world_projects/examples.py) | [`questions.md`](10_real_world_projects/questions.md) | Various Scripts | Newspaper Vendor Stock, SSMV School Roll Management, Pune Colleges NAAC Grade Tracking |
| **[11. MySQL & Databases](11_mysql/)** | — | [`mysql.sql`](11_mysql/mysql.sql) | — | [`ott_platform.sql`](11_mysql/ott_platform.sql) | `CREATE DATABASE`, `CREATE TABLE`, `INSERT INTO`, Multi-table OTT Platform Design (Netflix & Disney+) |
| **[12. For Loops & Iteration](12_for_loops/)** | [`explanation.md`](12_for_loops/explanation.md) | [`examples.py`](12_for_loops/examples.py) | [`questions.md`](12_for_loops/questions.md) | [`practice.py`](12_for_loops/practice.py) | `range()` variations, sequence iteration, `enumerate()`, `zip()`, `for-else`, nested patterns, even numbers, multiplication tables, real estate record iteration |

---

## 🔁 While Loop Problems

`while` loop problems are practised under **[04. Decision Making & Loops](04_control_flow/)** alongside `if/elif/else` and `for` loops.

### Problems Covered

| Problem | Core Technique | File |
| :--- | :--- | :--- |
| Factorial of a number | `while temp > 0: fact *= temp` | [`04_control_flow/examples.py`](04_control_flow/examples.py) |
| Countdown (10 → 1) | `while count > 0: count -= 1` | [`04_control_flow/practice.py`](04_control_flow/practice.py) |
| Loop control (`break` / `continue`) | Early exit & skip logic | [`04_control_flow/examples.py`](04_control_flow/examples.py) |
| `while-else` construct | `else` runs only on natural loop exit | [`04_control_flow/explanation.md`](04_control_flow/explanation.md) |
| Guard clause with `while True` | `while True: … if cond: break` | [`04_control_flow/practice.py`](04_control_flow/practice.py) |

### Quick Reference — `while` Loop Syntax

```python
# ── Basic while loop ──────────────────────────────────────────────
count = 1
while count <= 5:
    print(count)
    count += 1          # Always update to avoid infinite loop!

# ── Factorial using while ─────────────────────────────────────────
n = 6
fact = 1
temp = n
while temp > 0:
    fact *= temp
    temp -= 1
print(f"{n}! = {fact}")   # 6! = 720

# ── while-else construct ──────────────────────────────────────────
num = 10
while num > 0:
    print(num, end=" ")
    num -= 2
else:
    print("\nDone!")       # Runs ONLY if loop exits without break

# ── Infinite loop with break guard ───────────────────────────────
while True:
    user_input = input("Type 'quit' to exit: ")
    if user_input.lower() == "quit":
        break
```

---

## 📁 Repository Architecture

```tree
pyhton practice 7mentor/
├── 📜 README.md                        # Progress dashboard & topic navigator
├── 📁 01_basics/                       # Variables, Data Types, I/O, F-Strings
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 02_typecasting/                  # Primitive & collection typecasting, ASCII & base
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 03_operators/                    # Arithmetic, logical, bitwise, identity & membership
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 04_control_flow/                 # if/elif/else, while loops, for loops, leap year & prime
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py                  #  ← Factorial via while, car purchase nested-if
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 05_strings/                      # String slicing, methods, palindrome & vowel counter
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 06_lists/                        # List CRUD, sorting, filtering & comprehensions
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 07_tuples/                       # Immutability, unpacking & nested tuple operations
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 08_sets/                         # Mathematical sets, venn logic & frozensets
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 09_dictionaries/                 # Dictionary manipulation & frequency counters
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 10_real_world_projects/          # Real-world scenario mini-projects
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   ├── 🐍 newspaper_seller.py
│   ├── 🐍 ssmv_school.py
│   └── 🐍 pune_colleges_record.py
├── 📁 11_mysql/                        # MySQL database design & queries
│   ├── 🗄️ mysql.sql                   #  ← OTT Platform DB schema (Netflix & Disney+)
│   └── 🗄️ ott_platform.sql            #  ← Data insertion practice
└── 📁 12_for_loops/                    # For loop iterations, enumerate, zip, pattern printing
    ├── 📜 README.md
    ├── 📜 explanation.md
    ├── 🐍 examples.py
    ├── 📜 questions.md
    ├── 🐍 practice.py
    ├── 🐍 even_numbers.py              #  ← Print even 1–50 (3 approaches + sum)
    ├── 🐍 table_of_1000.py            #  ← Multiplication table of 1000 + dict iteration
    └── 🐍 real_estate_locations.py    #  ← Real estate record (dict + list of dicts)
```

---

## 🚀 Quick Start & Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Abhay2204/pyhton-practice-7mentor.git
   cd "pyhton practice 7mentor"
   ```

2. **Run Topic Examples & Practice Files**:
   ```bash
   # Basics & Fundamentals
   python 01_basics/examples.py
   python 01_basics/practice.py

   # Control Flow, while Loops & Leap Year
   python 04_control_flow/examples.py
   python 04_control_flow/practice.py

   # Data Structures
   python 05_strings/examples.py
   python 06_lists/examples.py
   python 07_tuples/examples.py
   python 08_sets/examples.py
   python 09_dictionaries/examples.py

   # Real World Projects
   python 10_real_world_projects/examples.py

   # For Loop Practice Files (new)
   python 12_for_loops/even_numbers.py
   python 12_for_loops/table_of_1000.py
   python 12_for_loops/real_estate_locations.py
   ```

---

## ✅ Skills & Concept Tracking Checklist

- [x] Topic-based folder modularization (`explanation.md`, `examples.py`, `questions.md`, `practice.py`)
- [x] Variable declaration & dynamic typing
- [x] Type casting (`int()`, `float()`, `str()`, `bool()`, ASCII & Base)
- [x] F-strings & numerical formatting
- [x] Arithmetic, comparison, logical, identity (`is`), membership (`in`), & bitwise operators
- [x] Conditional branches (`if`, `elif`, `else`) & Ternary operators
- [x] Leap year calculation (3 methods)
- [x] `for` loops, `range()` & `enumerate()`
- [x] `while` loops — Factorial, countdown, `while True` with `break`
- [x] `while-else` construct
- [x] `break`, `continue`, `pass` & `for-else` prime checks
- [x] String slicing, reversing, immutability & string methods
- [x] List CRUD, in-place sorting & list comprehensions
- [x] Tuple creation, packing & extended unpacking (`*tail`)
- [x] Mathematical Set operations (`|`, `&`, `-`, `^`), `discard` vs `remove`, & `frozenset`
- [x] Dictionary operations, safe lookup via `.get()`, & frequency counter algorithms
- [x] Real-world scenario problem solving (Inventory, Roll Tracking, College NAAC Grade Mapping)
- [x] Even numbers — 3 approaches (`range(step=2)`, `% 2 == 0` filter, list comprehension) + count & sum
- [x] Multiplication table generation via `for` loop (`table_of_1000.py`)
- [x] Real estate record iteration — dictionary with list & list of dictionaries
- [x] MySQL schema design — `CREATE TABLE`, `INSERT INTO`, multi-table OTT Platform

---

<div align="center">
  <sub>Maintained with ❤️ by <b>Abhay Mallick</b> as part of Python Training at 7Mentor.</sub>
</div>
