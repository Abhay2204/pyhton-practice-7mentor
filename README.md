# 🐍 Python 7Mentor Mastery & Practice Tracker

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Progress](https://img.shields.io/badge/Progress-100%25%20Completed-brightgreen.svg?style=for-the-badge&logo=checkmark)
![Modules](https://img.shields.io/badge/Topics-10%20Folders-orange.svg?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-purple.svg?style=for-the-badge)

<p align="center">
  <b>A comprehensive, production-grade Python practice repository organized into modular topic folders, each equipped with detailed concept explanations (`explanation.md`), working code demonstrations (`examples.py`), conceptual & coding questions (`questions.md`), and hands-on practice scripts (`practice.py`).</b>
</p>

[📌 Topic Modules](#-curriculum--topic-modules) •
[📁 Repository Architecture](#-repository-architecture) •
[🚀 Quick Start](#-quick-start--usage) •
[✅ Skill Checklist](#-skills--concept-tracking-checklist)

</div>

---

## 📈 Learning Progress & Topic Modules

```
Overall Syllabus Completion: [████████████████████████████████] 100%
```

| Topic / Folder | Explanation | Examples | Questions | Practice | Key Concepts Covered |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **[01. Basics & Fundamentals](01_basics/)** | [`explanation.md`](01_basics/explanation.md) | [`examples.py`](01_basics/examples.py) | [`questions.md`](01_basics/questions.md) | [`practice.py`](01_basics/practice.py) | Variables, Types, Dynamic Typing, F-Strings, Input/Output, Concatenation |
| **[02. Typecasting & Coercion](02_typecasting/)** | [`explanation.md`](02_typecasting/explanation.md) | [`examples.py`](02_typecasting/examples.py) | [`questions.md`](02_typecasting/questions.md) | [`practice.py`](02_typecasting/practice.py) | Implicit & Explicit Casting, Collection Conversion, Truthiness, ASCII & Base Conversions |
| **[03. Operator Mastery](03_operators/)** | [`explanation.md`](03_operators/explanation.md) | [`examples.py`](03_operators/examples.py) | [`questions.md`](03_operators/questions.md) | [`practice.py`](03_operators/practice.py) | Arithmetic, Relational, Short-Circuit Logical, Bitwise (`&`/`\|`/`^`/`~`), Identity (`is`), Membership (`in`) |
| **[04. Decision Making & Loops](04_control_flow/)** | [`explanation.md`](04_control_flow/explanation.md) | [`examples.py`](04_control_flow/examples.py) | [`questions.md`](04_control_flow/questions.md) | [`practice.py`](04_control_flow/practice.py) | `if/elif/else`, Leap Year (3 methods), Ternary, `range()`, `while`, Loop Control (`break`/`continue`), `for-else` |
| **[05. String Engineering](05_strings/)** | [`explanation.md`](05_strings/explanation.md) | [`examples.py`](05_strings/examples.py) | [`questions.md`](05_strings/questions.md) | [`practice.py`](05_strings/practice.py) | Immutability, Step Slicing, Case Methods, Search/Count, Strip, Split/Join, Palindrome & Vowels |
| **[06. Lists & Operations](06_lists/)** | [`explanation.md`](06_lists/explanation.md) | [`examples.py`](06_lists/examples.py) | [`questions.md`](06_lists/questions.md) | [`practice.py`](06_lists/practice.py) | Mutability, CRUD (`append`/`insert`/`extend`/`pop`/`remove`), `.sort()`, List Comprehension, Aggregations |
| **[07. Tuples & Immutability](07_tuples/)** | [`explanation.md`](07_tuples/explanation.md) | [`examples.py`](07_tuples/examples.py) | [`questions.md`](07_tuples/questions.md) | [`practice.py`](07_tuples/practice.py) | Single-element Tuples, Slicing, Immutability Workarounds, Packing & Extended Unpacking (`*tail`), Nested Tuples |
| **[08. Set Theory & Operations](08_sets/)** | [`explanation.md`](08_sets/explanation.md) | [`examples.py`](08_sets/examples.py) | [`questions.md`](08_sets/questions.md) | [`practice.py`](08_sets/practice.py) | Uniqueness, `.add()`, `.update()`, `.remove()` vs `.discard()`, Union (`\|`), Intersect (`&`), Diff (`-`), Sym-Diff (`^`), Frozenset |
| **[09. Dictionaries & Collections](09_dictionaries/)** | [`explanation.md`](09_dictionaries/explanation.md) | [`examples.py`](09_dictionaries/examples.py) | [`questions.md`](09_dictionaries/questions.md) | [`practice.py`](09_dictionaries/practice.py) | Key-Value Access, Safe `.get()`, Key/Value Iteration (`.items()`), Word Frequency Counter, Dict Comprehension |
| **[10. Real World Projects](10_real_world_projects/)** | [`explanation.md`](10_real_world_projects/explanation.md) | [`examples.py`](10_real_world_projects/examples.py) | [`questions.md`](10_real_world_projects/questions.md) | Various Scripts | Newspaper Vendor Stock, SSMV School Roll Management, Pune Colleges NAAC Grade Tracking |

---

## 📁 Repository Architecture

```tree
pyhton practice 7mentor/
├── 📜 README.md                    # Progress dashboard & topic navigator
├── 📁 01_basics/                   # Variables, Data Types, I/O, F-Strings
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 02_typecasting/              # Primitive & collection typecasting, ASCII & base conversions
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 03_operators/                # Arithmetic, logical, bitwise, identity & membership operators
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 04_control_flow/             # Decision logic, loops, leap year & prime algorithms
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 05_strings/                  # String slicing, methods, palindrome & vowel counter
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 06_lists/                    # Comprehensive list CRUD, sorting, filtering & comprehensions
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 07_tuples/                   # Immutability, unpacking & nested tuple operations
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 08_sets/                     # Mathematical sets, venn logic & frozensets
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 09_dictionaries/             # Dictionary manipulation & frequency counters
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
└── 📁 10_real_world_projects/     # Real-world scenario mini-projects
    ├── 📜 explanation.md
    ├── 🐍 examples.py
    ├── 📜 questions.md
    ├── 🐍 newspaper_seller.py
    ├── 🐍 ssmv_school.py
    └── 🐍 pune_colleges_record.py
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

   # Control Flow & Leap Year
   python 04_control_flow/examples.py

   # Data Structures
   python 05_strings/examples.py
   python 06_lists/examples.py
   python 07_tuples/examples.py
   python 08_sets/examples.py
   python 09_dictionaries/examples.py

   # Real World Projects
   python 10_real_world_projects/examples.py
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
- [x] `while` loops & factorials
- [x] `break`, `continue`, `pass` & `for-else` prime checks
- [x] String slicing, reversing, immutability & string methods
- [x] List CRUD, in-place sorting & list comprehensions
- [x] Tuple creation, packing & extended unpacking (`*tail`)
- [x] Mathematical Set operations (`|`, `&`, `-`, `^`), `discard` vs `remove`, & `frozenset`
- [x] Dictionary operations, safe lookup via `.get()`, & frequency counter algorithms
- [x] Real-world scenario problem solving (Inventory, Roll Tracking, College NAAC Grade Mapping)

---

<div align="center">
  <sub>Maintained with ❤️ by <b>Abhay Mallick</b> as part of Python Training at 7Mentor.</sub>
</div>
