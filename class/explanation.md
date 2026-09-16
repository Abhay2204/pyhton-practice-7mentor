# 16. Python Classes & Object-Oriented Programming (OOP)

## 📌 Overview
**Object-Oriented Programming (OOP)** is a programming paradigm that organizes software design around **data (attributes)** and **behavior (methods)** rather than functions and logic alone. 

A **Class** is a blueprint or template from which individual **Objects (instances)** are constructed.

---

## 🔑 Key Concepts

### 1. Class vs Object

| Concept | Definition | Analogy | Example |
| :--- | :--- | :--- | :--- |
| **Class** | Blueprint / Definition defining attributes & behaviors | Architectural blueprint of a house | `class Car:` |
| **Object** | Specific, concrete instance created from the class | Physical house built using that blueprint | `my_car = Car()` |

```python
# Defining a simple class
class Student:
    pass

# Creating objects (instantiation)
s1 = Student()
s2 = Student()
```

---

### 2. The `__init__` Constructor Method

The `__init__` method is the **constructor** in Python. It is called **automatically** whenever a new instance of the class is created.

```python
class Student:
    def __init__(self, name: str, roll_no: str, marks: float):
        # Initializing instance attributes
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
```

#### What is `self`?
- `self` represents the **current instance of the class**.
- When you call `s1 = Student("Rahul", "CS-101", 85)`, Python automatically converts it to:
  `Student.__init__(s1, "Rahul", "CS-101", 85)`.
- It binds the passed attributes to that specific instance (`self.name`, `self.roll_no`).

---

### 3. Types of Constructors

#### A. Parameterized Constructor
Takes parameters to initialize custom values for each instance:
```python
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role
```

#### B. Default / Non-Parameterized Constructor
Has only `self` or provides default parameter values:
```python
class DefaultConfig:
    def __init__(self, host="localhost", port=5000):
        self.host = host
        self.port = port
```

> [!NOTE]
> Python does **not** support multiple `__init__` methods in the same class (method overloading). The last defined `__init__` overwrites any earlier ones. To achieve multiple constructor patterns, use default arguments or `@classmethod` factory methods.

---

### 4. Instance Variables vs Class (Static) Variables

```python
class Employee:
    # Class Variable (shared by all instances)
    company_name = "Tech Corp"
    total_employees = 0

    def __init__(self, name, salary):
        # Instance Variables (unique to each object)
        self.name = name
        self.salary = salary
        Employee.total_employees += 1
```

- **Instance Variables**: Defined inside `__init__` using `self.variable_name`. Each object maintains its own independent copy.
- **Class Variables**: Defined directly inside the class body. Shared across all instances. Accessed via `ClassName.variable_name`.

---

### 5. Types of Methods

Python classes support three distinct categories of methods:

| Method Type | Decorator | First Argument | Purpose |
| :--- | :---: | :---: | :--- |
| **Instance Method** | None | `self` | Accesses & modifies instance state and attributes |
| **Class Method** | `@classmethod` | `cls` | Operates on the class itself; can access class variables |
| **Static Method** | `@staticmethod` | None | Independent utility function; does not access `self` or `cls` |

```python
class Calculator:
    version = "2.0"

    def __init__(self, owner):
        self.owner = owner

    # 1. Instance Method
    def print_owner(self):
        print(f"Calculator owner: {self.owner}")

    # 2. Class Method
    @classmethod
    def get_version(cls):
        return f"Version: {cls.version}"

    # 3. Static Method
    @staticmethod
    def add(a, b):
        return a + b
```

---

### 6. Special / Dunder Methods (`__str__` and `__repr__`)

- **`__str__(self)`**: Returns an informal, human-readable string representation of the object (used by `print()` and `str()`).
- **`__repr__(self)`**: Returns an official, unambiguous developer representation (used in debugging and terminal).

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"
```

---

### 7. Inheritance & `super()`

Inheritance allows a new class (**child / derived class**) to inherit attributes and methods from an existing class (**parent / base class**).

```python
# Base Class
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print(f"Name: {self.name}, Email: {self.email}")

# Child Class inheriting from Person
class Teacher(Person):
    def __init__(self, name, email, department):
        # Call parent constructor using super()
        super().__init__(name, email)
        self.department = department

    # Method Overriding
    def display(self):
        super().display()
        print(f"Department: {self.department}")
```

---

### 8. Encapsulation: Access Modifiers

Python uses naming conventions to signal visibility:

- **Public**: `self.name` (accessible everywhere)
- **Protected**: `self._account_id` (single underscore: internal use convention)
- **Private**: `self.__pin` (double underscore: triggers name mangling to `_ClassName__pin`)

```python
class BankAccount:
    def __init__(self, account_no, initial_balance):
        self.account_no = account_no
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):  # Getter method
        return self.__balance
```
