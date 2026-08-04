# 08. Set Theory & Operations in Python

## 📌 Overview
A Set is an **unordered**, **unindexed** collection of **unique** hashable elements, declared using curly braces `{}` or `set()`.

---

## 🔑 Key Concepts

### 1. Set Creation & Uniqueness
- An empty set **must** be created using `set()`, because `{}` creates an empty dictionary.
- Sets automatically eliminate duplicate elements.

### 2. Adding & Removing Elements
- `.add(elem)`: Adds a single element.
- `.update(iterable)`: Adds multiple elements from an iterable.
- `.remove(elem)`: Removes element; raises `KeyError` if absent.
- `.discard(elem)`: Removes element; **does not raise error** if absent.
- `.pop()`: Removes and returns an arbitrary element.

### 3. Mathematical Set Operations
| Operation | Operator | Method | Description |
| :--- | :---: | :--- | :--- |
| **Union** | `A \| B` | `A.union(B)` | Elements in A, B, or both |
| **Intersection** | `A & B` | `A.intersection(B)` | Elements common to both A and B |
| **Difference** | `A - B` | `A.difference(B)` | Elements in A but not in B |
| **Symmetric Diff** | `A ^ B` | `A.symmetric_difference(B)` | Elements in A or B, but NOT both |

### 4. Subsets & Frozensets
- `A.issubset(B)` / `A <= B`: Checks if all elements of A are in B.
- `A.isdisjoint(B)`: Returns `True` if A and B have no common elements.
- `frozenset(iterable)`: Immutable version of a set (can be used as dictionary key).
