# 🐍 Python 7Mentor Mastery & Practice Tracker

<div align="center">

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)
![Progress](https://img.shields.io/badge/Progress-In%20Progress-yellow.svg?style=for-the-badge)
![Modules](https://img.shields.io/badge/Topics-12%20Folders-orange.svg?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-purple.svg?style=for-the-badge)

<p align="center">
  <b>A comprehensive, production-grade Python practice repository organized into modular topic folders, each equipped with detailed concept explanations, working code demos, coding questions, and hands-on practice scripts.</b>
</p>

[📌 Topic Modules](#-learning-progress--topic-modules) •
[📁 Repository Architecture](#-repository-architecture) •
[📋 Python Quick Reference](#-python-quick-reference-cheatsheet) •
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
| **[04. Decision Making & Loops](04_control_flow/)** | [`explanation.md`](04_control_flow/explanation.md) | [`examples.py`](04_control_flow/examples.py) | [`questions.md`](04_control_flow/questions.md) | [`practice.py`](04_control_flow/practice.py) | `if/elif/else`, Leap Year (3 methods), Ternary, `range()`, `while` loops, Factorial, `break`/`continue`, `for-else` |
| **[05. String Engineering](05_strings/)** | [`explanation.md`](05_strings/explanation.md) | [`examples.py`](05_strings/examples.py) | [`questions.md`](05_strings/questions.md) | [`practice.py`](05_strings/practice.py) | Immutability, Step Slicing, Case Methods, Search/Count, Strip, Split/Join, Palindrome & Vowels |
| **[06. Lists & Operations](06_lists/)** | [`explanation.md`](06_lists/explanation.md) | [`examples.py`](06_lists/examples.py) | [`questions.md`](06_lists/questions.md) | [`practice.py`](06_lists/practice.py) | Mutability, CRUD (`append`/`insert`/`extend`/`pop`/`remove`), `.sort()`, List Comprehension, Aggregations |
| **[07. Tuples & Immutability](07_tuples/)** | [`explanation.md`](07_tuples/explanation.md) | [`examples.py`](07_tuples/examples.py) | [`questions.md`](07_tuples/questions.md) | [`practice.py`](07_tuples/practice.py) | Single-element Tuples, Slicing, Immutability Workarounds, Packing & Extended Unpacking (`*tail`), Nested Tuples |
| **[08. Set Theory & Operations](08_sets/)** | [`explanation.md`](08_sets/explanation.md) | [`examples.py`](08_sets/examples.py) | [`questions.md`](08_sets/questions.md) | [`practice.py`](08_sets/practice.py) | Uniqueness, `.add()`, `.update()`, `.remove()` vs `.discard()`, Union (`\|`), Intersect (`&`), Diff (`-`), Sym-Diff (`^`), Frozenset |
| **[09. Dictionaries & Collections](09_dictionaries/)** | [`explanation.md`](09_dictionaries/explanation.md) | [`examples.py`](09_dictionaries/examples.py) | [`questions.md`](09_dictionaries/questions.md) | [`practice.py`](09_dictionaries/practice.py) | Key-Value Access, Safe `.get()`, Key/Value Iteration (`.items()`), Word Frequency Counter, Dict Comprehension |
| **[10. Real World Projects](10_real_world_projects/)** | [`explanation.md`](10_real_world_projects/explanation.md) | [`examples.py`](10_real_world_projects/examples.py) | [`questions.md`](10_real_world_projects/questions.md) | Various Scripts | Newspaper Vendor Stock, SSMV School Roll Management, Pune Colleges NAAC Grade Tracking |
| **[11. MySQL & Databases](11_mysql/)** | — | [`mysql.sql`](11_mysql/mysql.sql) | — | [`ott_platform.sql`](11_mysql/ott_platform.sql) | `CREATE`, `INSERT`, `SELECT`, `WHERE`, `AND/OR/LIKE/BETWEEN/IN`, `ORDER BY`, `LIMIT`, `GROUP BY`, `HAVING`, `UPDATE`, `DELETE`, `ALTER`, Aggregate Functions |
| **[12. For Loops & Iteration](12_for_loops/)** | [`explanation.md`](12_for_loops/explanation.md) | [`examples.py`](12_for_loops/examples.py) | [`questions.md`](12_for_loops/questions.md) | [`practice.py`](12_for_loops/practice.py) | `range()` variations, sequence iteration, `enumerate()`, `zip()`, `for-else`, nested patterns, even numbers, multiplication tables, real estate record iteration |

---

## 📋 Python Quick Reference Cheatsheet

### 🔀 Conditions (`if` / `elif` / `else`)
```python
age = 20

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")

# Ternary (one-liner)
status = "Adult" if age >= 18 else "Minor"
```

---

### 🔁 Loops

**`for` loop**
```python
# Loop over a range
for i in range(1, 6):
    print(i)           # 1 2 3 4 5

# Loop with step
for i in range(0, 11, 2):
    print(i)           # 0 2 4 6 8 10

# Loop over a list
fruits = ["Apple", "Mango", "Cherry"]
for fruit in fruits:
    print(fruit)

# enumerate() — loop with index
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# zip() — loop over two lists together
names  = ["Abhay", "Rohit"]
marks  = [88, 72]
for name, mark in zip(names, marks):
    print(f"{name}: {mark}")
```

**`while` loop**
```python
count = 1
while count <= 5:
    print(count)
    count += 1

# while with break
while True:
    ans = input("Type quit to exit: ")
    if ans == "quit":
        break
```

**Loop control**
```python
for i in range(1, 11):
    if i == 5:
        continue    # skip 5
    if i == 8:
        break       # stop at 8
    print(i)
```

---

### 🔧 Functions (`def`)
```python
# Define and call
def greet(name):
    print(f"Hello, {name}!")

greet("Abhay")

# With return value
def add(a, b):
    return a + b

result = add(3, 5)   # 8

# Default argument
def power(base, exp=2):
    return base ** exp

print(power(4))      # 16
print(power(2, 3))   # 8
```

---

### 📝 Strings
```python
s = "Hello, Python!"

print(s.upper())          # HELLO, PYTHON!
print(s.lower())          # hello, python!
print(s.strip())          # remove leading/trailing spaces
print(s.replace("Python", "World"))
print(s.split(", "))      # ['Hello', 'Python!']
print(len(s))             # 14
print(s[0:5])             # Hello   (slicing)
print(s[::-1])            # !nohtyP ,olleH  (reverse)
print("py" in s)          # False  (membership)
print(s.startswith("He")) # True
print(s.count("l"))       # 3
```

---

### 📋 Lists
```python
nums = [10, 20, 30]

nums.append(40)           # [10, 20, 30, 40]
nums.insert(1, 15)        # [10, 15, 20, 30, 40]
nums.extend([50, 60])     # adds multiple items
nums.remove(15)           # removes first occurrence of 15
nums.pop()                # removes & returns last item
nums.pop(0)               # removes item at index 0
nums.sort()               # sort ascending in-place
nums.sort(reverse=True)   # sort descending
nums.reverse()            # reverse in-place
print(len(nums))          # length
print(nums[0])            # first element
print(nums[-1])           # last element
print(nums[1:3])          # slicing

# List comprehension
squares = [x**2 for x in range(1, 6)]   # [1, 4, 9, 16, 25]
evens   = [x for x in range(1, 21) if x % 2 == 0]
```

---

### 📦 Tuples
```python
t = (10, 20, 30, 40)

print(t[0])          # 10  (indexing)
print(t[-1])         # 40
print(t[1:3])        # (20, 30)  (slicing)
print(len(t))        # 4
print(t.count(20))   # 1
print(t.index(30))   # 2

# Packing & Unpacking
a, b, c, d = t
first, *rest = t     # first=10, rest=[20, 30, 40]

# Single-element tuple needs a trailing comma
single = (42,)
```

---

### 🔵 Sets
```python
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

s1.add(5)            # add one element
s1.update([6, 7])    # add multiple
s1.remove(7)         # raises error if missing
s1.discard(99)       # safe remove — no error if missing

print(s1 | s2)       # Union
print(s1 & s2)       # Intersection
print(s1 - s2)       # Difference
print(s1 ^ s2)       # Symmetric Difference

fs = frozenset([1, 2, 3])   # immutable set
```

---

### 📖 Dictionaries
```python
student = {"name": "Abhay", "age": 21, "city": "Pune"}

print(student["name"])          # Abhay
print(student.get("grade", "N/A"))  # safe access with default

student["marks"] = 88           # add/update key
del student["city"]             # delete key

for key, value in student.items():
    print(f"{key}: {value}")

print(student.keys())           # dict_keys
print(student.values())         # dict_values
print("name" in student)        # True

# Dict comprehension
squares = {x: x**2 for x in range(1, 6)}
```

---

### 🗄️ MySQL Quick Reference
```sql
-- Create & use database
CREATE DATABASE school_db;
USE school_db;

-- Create table
CREATE TABLE students (
    id    INT PRIMARY KEY AUTO_INCREMENT,
    name  VARCHAR(100),
    marks FLOAT
);

-- Insert data
INSERT INTO students (name, marks) VALUES ('Abhay', 88.5);

-- Select & filter
SELECT * FROM students WHERE marks > 80 ORDER BY marks DESC LIMIT 5;

-- Aggregate functions
SELECT COUNT(*), AVG(marks), MAX(marks), MIN(marks) FROM students;

-- Group by
SELECT city, COUNT(*) FROM students GROUP BY city HAVING COUNT(*) > 2;

-- Update & Delete
UPDATE students SET marks = 95 WHERE name = 'Abhay';
DELETE FROM students WHERE marks < 40;
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
├── 📁 02_typecasting/                  # Primitive & collection typecasting
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 03_operators/                    # Arithmetic, logical, bitwise operators
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 04_control_flow/                 # if/elif/else, while, for, leap year & prime
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 05_strings/                      # String slicing, methods, palindrome
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 06_lists/                        # List CRUD, sorting, comprehensions
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 07_tuples/                       # Immutability, unpacking, nested tuples
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 08_sets/                         # Set theory, venn logic, frozensets
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 🐍 questions.md
│   ├── 🐍 practice.py
│   ├── 🐍 set_loop.py
│   └── 🐍 set_practice.py
├── 📁 09_dictionaries/                 # Dictionary manipulation & frequency counters
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   └── 🐍 practice.py
├── 📁 10_real_world_projects/          # Real-world scenario mini-projects
│   ├── 📜 explanation.md
│   ├── 🐍 examples.py
│   ├── 📜 questions.md
│   ├── 🐍 maharashtra_election.py
│   ├── 🐍 newspaper_seller.py
│   ├── 🐍 pune_colleges_record.py
│   ├── 🐍 real_estate_record.py
│   └── 🐍 ssmv_school.py
├── 📁 11_mysql/                        # MySQL — all topics before JOINs
│   ├── 🗄️ mysql.sql                   # CREATE, INSERT, SELECT, WHERE, GROUP BY, UPDATE, ALTER
│   └── 🗄️ ott_platform.sql            # OTT Platform practice data
└── 📁 12_for_loops/                    # For loop iterations, enumerate, zip, patterns
    ├── 📜 README.md
    ├── 📜 explanation.md
    ├── 🐍 examples.py
    ├── 📜 questions.md
    ├── 🐍 practice.py
    ├── 🐍 even_numbers.py
    ├── 🐍 table_of_124.py
    ├── 🐍 table_of_1000.py
    └── 🐍 real_estate_locations.py
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
   python 01_basics/examples.py
   python 04_control_flow/examples.py
   python 05_strings/examples.py
   python 06_lists/examples.py
   python 07_tuples/examples.py
   python 08_sets/examples.py
   python 09_dictionaries/examples.py
   python 12_for_loops/even_numbers.py
   python 12_for_loops/table_of_124.py
   python 12_for_loops/real_estate_locations.py
   ```

---

## ✅ Skills & Concept Tracking Checklist

- [x] Variable declaration & dynamic typing
- [x] Type casting — `int()`, `float()`, `str()`, `bool()`, ASCII & Base
- [x] F-strings & numerical formatting
- [x] Arithmetic, comparison, logical, identity (`is`), membership (`in`), bitwise operators
- [x] Conditional branches — `if`, `elif`, `else` & Ternary
- [x] Leap year calculation (3 methods)
- [x] `for` loops — `range()`, `enumerate()`, `zip()`, `for-else`
- [x] `while` loops — countdown, factorial, `while True` with `break`
- [x] Loop control — `break`, `continue`, `pass`
- [x] String methods — `upper/lower/strip/replace/split/join/count/find`
- [x] List CRUD — `append`, `insert`, `extend`, `pop`, `remove`, `sort`, `reverse`
- [x] List comprehension with conditions
- [x] Tuple creation, packing, slicing & extended unpacking (`*tail`)
- [x] Set operations — Union, Intersection, Difference, Symmetric Difference, Frozenset
- [x] Dictionary — `.get()`, `.items()`, `.keys()`, `.values()`, dict comprehension
- [x] Real-world projects — Inventory, Roll Tracking, College NAAC Grade Mapping
- [x] MySQL — `CREATE`, `INSERT`, `SELECT`, `WHERE`, `AND/OR/LIKE/BETWEEN/IN`
- [x] MySQL — `ORDER BY`, `LIMIT`, `GROUP BY`, `HAVING`, `UPDATE`, `DELETE`, `ALTER`
- [x] MySQL — Aggregate functions — `COUNT`, `AVG`, `MAX`, `MIN`, `SUM`

---

<div align="center">
  <sub>Maintained with ❤️ by <b>Abhay Mallick</b> as part of Python Training at 7Mentor.</sub>
</div>

