# 🏛️ 16. Python Classes & Object-Oriented Programming (OOP)

Welcome to the **Classes and Object-Oriented Programming Module** of the 7Mentor Python Mastery series. Object-Oriented Programming (OOP) is the core paradigm used in modern software engineering to model real-world domains with encapsulated state and behaviors.

---

## 📑 Module Contents

| File | Type | Description |
| :--- | :---: | :--- |
| [`explanation.md`](explanation.md) | 📖 Guide | In-depth theory: classes, objects, `__init__` constructor, `self`, instance vs class variables, methods, dunder methods (`__str__`/`__repr__`), inheritance, and encapsulation. |
| [`examples.py`](examples.py) | 💻 Code | Fully runnable demonstrations of classes, constructors, methods, method resolution, dunder methods, and access control. |
| [`questions.md`](questions.md) | ❓ Q&A | 20+ conceptual interview questions, output prediction traps, and solved coding challenges. |
| [`practice.py`](practice.py) | 🏋️ Practice | Hands-on exercises: Student Academic Profile, Bank Account, Vehicle & EV Inheritance, and Library Management. |

---

## 🔑 Quick Concept Summary

```
                +------------------------------------+
                |            class Student:          |  <-- Class Definition (Blueprint)
                |                                    |
                |  def __init__(self, name, roll):   |  <-- Constructor (__init__)
                |      self.name = name              |  <-- Instance Variable
                |      self.roll = roll              |
                |                                    |
                |  def introduce(self):              |  <-- Instance Method
                |      return f"I am {self.name}"    |
                +------------------------------------+
                                  |
                                  | Instantiation
                                  v
                +------------------------------------+
                | s1 = Student("Rahul", "CS-101")    |  <-- Object / Instance in Memory
                +------------------------------------+
```

1. **Class vs Object**: A class is the architectural template; an object is the active instance in memory.
2. **`__init__` Constructor**: Executes automatically upon object creation to set initial state.
3. **`self` Parameter**: The explicit reference to the current instance invoking the method.
4. **Instance vs Class Variables**:
   - `self.variable`: Unique to each instance.
   - `ClassName.variable`: Shared across all instances of the class.
5. **Inheritance & `super()`**: Child classes inherit attributes and methods from parent classes using `super().__init__(...)`.

---

## 🚀 How to Run the Scripts

From the repository root:

```bash
# Run concept demonstrations
python 16_classes/examples.py

# Run hands-on practice exercises
python 16_classes/practice.py
```
