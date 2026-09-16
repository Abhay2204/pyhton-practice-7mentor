"""
16. Python Classes & Object-Oriented Programming (OOP) — Code Demonstrations
Run this file to see live demonstrations of all key OOP concepts:
python 16_classes/examples.py
"""


def section(title):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)


# ============================================================
# 1. Basic Class and Object Creation
# ============================================================
section("1. Basic Class and Object Creation")


class SimpleStudent:
    pass


s1 = SimpleStudent()
s2 = SimpleStudent()

# Manually assigning attributes
s1.name = "Rahul"
s1.roll_no = "CS-101"

print(f"s1 Object: {s1}")
print(f"s1 Attributes: name={s1.name}, roll_no={s1.roll_no}")
print(f"Is s1 an instance of SimpleStudent? {isinstance(s1, SimpleStudent)}")


# ============================================================
# 2. Constructor (__init__) and Instance Attributes
# ============================================================
section("2. Constructor (__init__) and Instance Attributes")


class Student:
    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def introduce(self):
        return f"Hi, I am {self.name} ({self.roll_no}), studying {self.course}."


student_a = Student("Maya Joshi", "CS-204", "Computer Engineering")
student_b = Student("Amit Sharma", "IT-105", "Information Technology")

print(student_a.introduce())
print(student_b.introduce())


# ============================================================
# 3. Default Arguments in Constructor
# ============================================================
section("3. Default Arguments in Constructor")


class UserProfile:
    def __init__(self, username, role="student", is_active=True):
        self.username = username
        self.role = role
        self.is_active = is_active

    def get_status(self):
        status = "Active" if self.is_active else "Suspended"
        return f"User: {self.username} | Role: {self.role} | Status: {status}"


u1 = UserProfile("admin", role="admin")
u2 = UserProfile("rohit_99")  # uses default role="student", is_active=True

print(u1.get_status())
print(u2.get_status())


# ============================================================
# 4. Instance Variables vs Class (Static) Variables
# ============================================================
section("4. Instance Variables vs Class Variables")


class Employee:
    # Class Variable (shared by all employee objects)
    company_name = "7Mentor Tech Labs"
    total_employees = 0

    def __init__(self, emp_id, name, department):
        # Instance Variables (unique to each employee)
        self.emp_id = emp_id
        self.name = name
        self.department = department

        # Increment class variable whenever a new object is created
        Employee.total_employees += 1

    def display(self):
        print(f"[{self.emp_id}] {self.name} | Dept: {self.department} | Company: {self.company_name}")


e1 = Employee("EMP01", "Pooja Patil", "Development")
e2 = Employee("EMP02", "Suresh Deshmukh", "Quality Assurance")

e1.display()
e2.display()
print(f"Total employees hired: {Employee.total_employees}")


# ============================================================
# 5. Instance Methods, Class Methods, and Static Methods
# ============================================================
section("5. Instance, Class, and Static Methods")


class BankService:
    bank_name = "State Academic Bank"
    interest_rate = 6.5

    def __init__(self, customer_name, balance):
        self.customer_name = customer_name
        self.balance = balance

    # 1. Instance Method (uses `self` to access object data)
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited Rs. {amount}. New Balance: Rs. {self.balance}"
        return "Invalid amount."

    # 2. Class Method (uses `cls` to access class variables)
    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        return f"Updated bank interest rate to {cls.interest_rate}%"

    # 3. Static Method (independent utility function, no self or cls)
    @staticmethod
    def calculate_simple_interest(principal, rate, years):
        return (principal * rate * years) / 100


account = BankService("Aditi Kulkarni", 15000)
print(account.deposit(5000))
print(BankService.set_interest_rate(7.0))

si = BankService.calculate_simple_interest(20000, BankService.interest_rate, 2)
print(f"Simple interest for 2 years on Rs. 20000 at {BankService.interest_rate}%: Rs. {si}")


# ============================================================
# 6. String Representations: __str__ and __repr__
# ============================================================
section("6. Special Dunder Methods: __str__ and __repr__")


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        # Friendly readable string for end-users
        return f"'{self.title}' by {self.author} (Rs. {self.price})"

    def __repr__(self):
        # Unambiguous representation for developers & debugging
        return f"Book(title='{self.title}', author='{self.author}', price={self.price})"


b = Book("Fluent Python", "Luciano Ramalho", 1450)
print("Using print() / str() :", str(b))
print("Using repr()          :", repr(b))


# ============================================================
# 7. Inheritance & super() Constructor Chaining
# ============================================================
section("7. Inheritance & super() Constructor Chaining")


class User:
    def __init__(self, username, email, role):
        self.username = username
        self.email = email
        self.role = role

    def get_info(self):
        return f"User: {self.username} [{self.role}] - {self.email}"


class Teacher(User):
    def __init__(self, username, email, department, subjects):
        # Call parent constructor
        super().__init__(username, email, role="teacher")
        self.department = department
        self.subjects = subjects

    # Method Overriding: customize behavior for child class
    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} | Dept: {self.department} | Teaching: {', '.join(self.subjects)}"


t = Teacher("anita_p", "anita@campus.edu", "Computer Science", ["Python", "Data Structures"])
print(t.get_info())


# ============================================================
# 8. Encapsulation: Private Attributes and Getters/Setters
# ============================================================
section("8. Encapsulation: Private Attributes")


class SecureAccount:
    def __init__(self, account_no, initial_balance):
        self.account_no = account_no
        self.__balance = initial_balance  # Private attribute (double underscore)

    def get_balance(self):
        """Getter method"""
        return self.__balance

    def deposit(self, amount):
        """Setter with validation"""
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False


acc = SecureAccount("ACC-9876", 5000)
print(f"Account: {acc.account_no}")
print(f"Balance via getter: Rs. {acc.get_balance()}")

acc.deposit(2500)
print(f"Balance after Rs. 2500 deposit: Rs. {acc.get_balance()}")

acc.withdraw(1000)
print(f"Balance after Rs. 1000 withdrawal: Rs. {acc.get_balance()}")

# Trying to access private variable directly raises AttributeError:
try:
    print(acc.__balance)
except AttributeError as err:
    print(f"Direct access blocked! -> {err}")


if __name__ == "__main__":
    print("\nAll OOP examples completed successfully!")
