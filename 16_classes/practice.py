"""
16. Python Classes & Object-Oriented Programming (OOP) — Practice Exercises
Hands-on exercises covering classes, constructors, methods, and inheritance.
Run this file to verify all exercises:
python 16_classes/practice.py
"""


# ============================================================
# Exercise 1: Student Academic Profile Class
# ============================================================
class StudentRecord:
    def __init__(self, name, roll_no, college):
        self.name = name
        self.roll_no = roll_no
        self.college = college
        self.marks = {}

    def add_subject_mark(self, subject, marks):
        self.marks[subject] = float(marks)

    def calculate_percentage(self):
        if not self.marks:
            return 0.0
        total_obtained = sum(self.marks.values())
        max_possible = len(self.marks) * 100
        return round((total_obtained / max_possible) * 100, 2)

    def get_grade(self):
        pct = self.calculate_percentage()
        if pct >= 90:
            return "A+"
        elif pct >= 80:
            return "A"
        elif pct >= 70:
            return "B"
        elif pct >= 60:
            return "C"
        elif pct >= 40:
            return "Pass"
        else:
            return "Fail"

    def generate_report(self):
        print(f"\n--- Report Card: {self.name} ({self.roll_no}) ---")
        print(f"College: {self.college}")
        for sub, sc in self.marks.items():
            print(f"  • {sub}: {sc}/100")
        pct = self.calculate_percentage()
        grade = self.get_grade()
        print(f"Overall: {pct}% | Final Grade: {grade}")


# ============================================================
# Exercise 2: Bank Account Class with Transaction History
# ============================================================
class BankAccount:
    def __init__(self, account_no, holder_name, initial_balance=0.0):
        self.account_no = account_no
        self.holder_name = holder_name
        self.balance = float(initial_balance)
        self.transactions = []
        if initial_balance > 0:
            self.transactions.append(f"Initial deposit: +Rs. {initial_balance}")

    def deposit(self, amount):
        if amount <= 0:
            return False, "Deposit amount must be positive."
        self.balance += amount
        self.transactions.append(f"Deposited: +Rs. {amount}")
        return True, f"Deposited Rs. {amount}. Balance: Rs. {self.balance}"

    def withdraw(self, amount):
        if amount <= 0:
            return False, "Withdrawal amount must be positive."
        if amount > self.balance:
            return False, "Insufficient funds."
        self.balance -= amount
        self.transactions.append(f"Withdrew: -Rs. {amount}")
        return True, f"Withdrew Rs. {amount}. Balance: Rs. {self.balance}"

    def get_statement(self):
        print(f"\n--- Statement for {self.holder_name} (Acc: {self.account_no}) ---")
        for tx in self.transactions:
            print(f"  {tx}")
        print(f"Current Balance: Rs. {self.balance}")


# ============================================================
# Exercise 3: Vehicle & Electric Car (Inheritance)
# ============================================================
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def drive(self, kilometers):
        if kilometers > 0:
            self.odometer += kilometers
            print(f"Drove {kilometers} km. Total odometer: {self.odometer} km")

    def get_specs(self):
        return f"{self.year} {self.make} {self.model} ({self.odometer} km)"


class ElectricCar(Vehicle):
    def __init__(self, make, model, year, battery_capacity_kwh):
        super().__init__(make, model, year)
        self.battery_capacity_kwh = battery_capacity_kwh
        self.charge_level = 100

    def drive(self, kilometers):
        needed_charge = kilometers * 0.2
        if needed_charge > self.charge_level:
            print("Not enough battery to complete this journey! Please recharge.")
            return
        super().drive(kilometers)
        self.charge_level -= needed_charge
        print(f"Remaining Battery: {self.charge_level:.1f}%")

    def recharge(self):
        self.charge_level = 100
        print("Battery fully recharged to 100%.")


# ============================================================
# Exercise 4: Library Book Inventory System
# ============================================================
class BookItem:
    def __init__(self, isbn, title, author):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"[{self.isbn}] '{self.title}' by {self.author} ({status})"


class Library:
    def __init__(self, library_name):
        self.library_name = library_name
        self.books = []

    def add_book(self, isbn, title, author):
        book = BookItem(isbn, title, author)
        self.books.append(book)
        print(f"Added book: '{title}'")

    def borrow_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                if b.is_borrowed:
                    return False, f"'{b.title}' is currently checked out."
                b.is_borrowed = True
                return True, f"Successfully checked out '{b.title}'."
        return False, "Book not found in library catalogue."

    def return_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                if not b.is_borrowed:
                    return False, f"'{b.title}' was not borrowed."
                b.is_borrowed = False
                return True, f"Successfully returned '{b.title}'."
        return False, "Book not found."

    def display_books(self):
        print(f"\n--- Catalogue: {self.library_name} ---")
        for b in self.books:
            print(f"  {b}")


# ============================================================
# Demonstration & Self-Test Runner
# ============================================================
if __name__ == "__main__":
    print("=== Exercise 1: Student Record ===")
    s = StudentRecord("Neha Deshpande", "CS-302", "COEP Pune")
    s.add_subject_mark("Python", 92)
    s.add_subject_mark("Database Systems", 88)
    s.add_subject_mark("Operating Systems", 85)
    s.generate_report()

    print("\n=== Exercise 2: Bank Account ===")
    acc = BankAccount("SBI-0012", "Rohan Mehta", 10000)
    acc.deposit(3500)
    acc.withdraw(2000)
    acc.get_statement()

    print("\n=== Exercise 3: Vehicle & ElectricCar Inheritance ===")
    ev = ElectricCar("Tata", "Nexon EV", 2024, battery_capacity_kwh=40)
    print(ev.get_specs())
    ev.drive(50)
    ev.drive(100)

    print("\n=== Exercise 4: Library Management System ===")
    lib = Library("Campus Central Library")
    lib.add_book("ISBN-101", "Introduction to Algorithms", "CLRS")
    lib.add_book("ISBN-102", "Learning Python", "Mark Lutz")
    lib.display_books()
    ok, msg = lib.borrow_book("ISBN-101")
    print(msg)
    lib.display_books()

    print("\nAll practice exercises executed successfully!")
