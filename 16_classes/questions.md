# ❓ Python Classes & Object-Oriented Programming (OOP): Q&A & Interview Prep

Comprehensive theoretical questions, output predictions, and coding challenges designed for interview and viva preparation.

---

## 📌 Part 1: Conceptual & Interview Questions

### Q1. What is the fundamental difference between a Class and an Object?
**Answer:**
- A **Class** is a user-defined prototype or blueprint defining attributes (variables) and behaviors (methods) common to all entities of that type. It does not occupy memory space for instance data.
- An **Object** is an actual physical instance of the class created in memory during runtime. Multiple independent objects can be instantiated from a single class.

---

### Q2. What is the purpose of the `__init__` method in Python? Is it technically a constructor?
**Answer:**
- `__init__` is an **initialization method** that executes automatically immediately after an object is instantiated in memory.
- In Python, `__new__` is the actual constructor that allocates memory and creates the instance, whereas `__init__` initializes the instance's attributes with initial state.
- In common Python terminology, `__init__` is widely referred to as the constructor.

---

### Q3. What is the `self` parameter in Python methods? Can it be renamed?
**Answer:**
- `self` is an explicit reference to the **current instance** of the class. It allows methods to access and modify the specific instance's attributes and methods.
- When an instance method is called like `student.study()`, Python automatically passes the instance as the first argument: `Student.study(student)`.
- Yes, `self` is not a Python reserved keyword—it is a strong community convention (PEP 8). You could technically name it `this` or `me`, but doing so violates PEP 8 and harms code readability.

---

### Q4. Does Python support Constructor Overloading (multiple `__init__` methods)?
**Answer:**
**No.** Python does not support multiple `__init__` methods in the same class. If multiple `__init__` methods are written, the **last defined one overwrites all previous ones**.

**Workaround patterns:**
1. **Default argument values**:
   ```python
   class Person:
       def __init__(self, name, age=0):
           self.name = name
           self.age = age
   ```
2. **Variable-length arguments (`*args`, `**kwargs`)**:
   ```python
   class Point:
       def __init__(self, *coords):
           self.coords = coords
   ```
3. **Class methods as alternative constructors (`@classmethod`)**:
   ```python
   class Date:
       def __init__(self, day, month, year):
           self.day, self.month, self.year = day, month, year

       @classmethod
       def from_string(cls, date_str):  # "16-09-2026"
           d, m, y = map(int, date_str.split("-"))
           return cls(d, m, y)
   ```

---

### Q5. What is the difference between an Instance Variable and a Class (Static) Variable?
**Answer:**
| Feature | Instance Variable | Class Variable |
| :--- | :--- | :--- |
| **Declaration** | Inside methods (usually `__init__`) using `self.var` | Directly in the class body |
| **Scope & Memory** | Unique copy for every instance | Shared single copy among all instances |
| **Access** | Via instance (`self.var` or `obj.var`) | Via class name (`Class.var`) or instance |

---

### Q6. What is the difference between `@classmethod` and `@staticmethod`?
**Answer:**
- **`@classmethod`**:
  - Takes `cls` (the class object itself) as its mandatory first argument.
  - Can inspect and modify class-level state.
  - Often used as factory constructors.
- **`@staticmethod`**:
  - Takes neither `self` nor `cls`.
  - Becomes a standard function bound to the class's namespace for logical grouping.
  - Cannot access or modify instance or class state.

---

### Q7. What does `super()` do in Python?
**Answer:**
`super()` returns a proxy object that delegates method calls to a parent or sibling class in the inheritance hierarchy (MRO - Method Resolution Order). It is most frequently used to invoke the parent class's `__init__` method:

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Passes name to Parent constructor
        self.age = age
```

---

### Q8. How does Python implement Private attributes (Encapsulation)? What is Name Mangling?
**Answer:**
Prefixing an attribute with two leading underscores (`__private_var`) triggers **name mangling**. Python internally rewrites `__private_var` to `_ClassName__private_var`.
This prevents accidental overwriting in subclasses and warns other developers against direct external modification.

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance

a = Account(1000)
# a.__balance -> Raises AttributeError
# a._Account__balance -> Accessible through mangled name (1000)
```

---

## 💻 Part 2: Output Prediction Questions

### Code Snippet 1
```python
class Demo:
    count = 0
    def __init__(self):
        Demo.count += 1

d1 = Demo()
d2 = Demo()
d3 = Demo()
print(Demo.count, d1.count)
```
**Output:**
```
3 3
```
**Explanation:** `Demo.count` is a class variable incremented on every `__init__` call. When accessing `d1.count`, Python first looks on the instance `d1`. Not finding it, it looks up to the class `Demo`, returning `3`.

---

### Code Snippet 2: The Mutable Class Variable Trap
```python
class Box:
    items = []  # Mutable class variable (DANGER!)
    def add(self, item):
        self.items.append(item)

b1 = Box()
b2 = Box()
b1.add("Notebook")
print(b2.items)
```
**Output:**
```
['Notebook']
```
**Explanation:** `items` is a list defined at the class level. Because lists are mutable, both `b1` and `b2` share the exact same list object in memory. To avoid this, always initialize mutable attributes inside `__init__`: `self.items = []`.

---

### Code Snippet 3
```python
class Parent:
    def greet(self):
        return "Hello from Parent"

class Child(Parent):
    def greet(self):
        return super().greet() + " and Child"

c = Child()
print(c.greet())
```
**Output:**
```
Hello from Parent and Child
```
**Explanation:** `super().greet()` executes the parent method, and the result is concatenated with the child string.

---

## 🏆 Part 3: Coding Challenges

### Challenge 1: Rectangle Area & Perimeter Class
**Task:** Create a class `Rectangle` with length and width, returning area and perimeter, plus an `is_square()` check.

```python
class Rectangle:
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def is_square(self):
        return self.length == self.width
```

---

### Challenge 2: Bank Account with Transfer Power
**Task:** Create a `BankAccount` class with account transfer functionality between two accounts.

```python
class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer_to(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True, f"Transferred Rs. {amount} to {target_account.owner}"
        return False, "Transfer failed: Insufficient balance."
```
