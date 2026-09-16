"""
=============================================================================
Topic: 14_functions - Comprehensive Python Functions Examples
Demonstrations of function definitions, argument parsing, LEGB scope,
closures, lambdas, recursion, and modular composition.
=============================================================================
"""

from functools import reduce

# ============================================================================
# 1. Basic Function Definition & Multiple Returns
# ============================================================================
def calculate_metrics(numbers: list):
    """Calculates min, max, sum, and average of a numeric list."""
    if not numbers:
        return 0, 0, 0, 0.0
    total = sum(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    average = total / len(numbers)
    # Returning multiple values as a tuple (packing)
    return minimum, maximum, total, round(average, 2)


# ============================================================================
# 2. Argument Variations: Positional, Keyword, & Defaults
# ============================================================================
def generate_receipt(customer: str, total_amount: float, discount: float = 0.0, tax_rate: float = 0.05):
    """Calculates final billing with optional discount and standard tax."""
    discounted = total_amount * (1 - discount)
    final_bill = discounted * (1 + tax_rate)
    return {
        "customer": customer,
        "base": total_amount,
        "discount_applied": f"{discount * 100}%",
        "tax_rate": f"{tax_rate * 100}%",
        "final_payable": round(final_bill, 2),
    }


# ============================================================================
# 3. Pitfall: Avoid Mutable Default Arguments
# ============================================================================
# Bad: def add_item_bad(item, inventory=[]) -> shares same list across invocations!
def add_item_safe(item: str, inventory=None):
    """Idiomatic way to handle mutable default parameters."""
    if inventory is None:
        inventory = []
    inventory.append(item)
    return inventory


# ============================================================================
# 4. Variable-Length Arguments (*args & **kwargs)
# ============================================================================
def build_employee_record(emp_id: int, name: str, *certifications, **additional_details):
    """
    *certifications gathers extra positional values into a tuple.
    **additional_details gathers keyword arguments into a dictionary.
    """
    record = {
        "id": emp_id,
        "name": name,
        "certifications": list(certifications),
        "details": additional_details,
    }
    return record


# ============================================================================
# 5. Variable Scope & LEGB Hierarchy (Local, Enclosing, Global, Built-in)
# ============================================================================
app_version = "1.0.0"  # Global scope

def outer_counter():
    """Demonstrates enclosing scope and nonlocal variable modification."""
    count = 0  # Enclosing scope

    def increment():
        nonlocal count  # Rebinds variable in nearest enclosing scope
        count += 1
        return count

    return increment


# ============================================================================
# 6. Anonymous (Lambda) Functions & Higher-Order Functions
# ============================================================================
def functional_programming_demo():
    scores = [45, 88, 72, 95, 33, 60, 91]
    
    # Filter passing scores (>= 60)
    passing_scores = list(filter(lambda score: score >= 60, scores))
    
    # Map curved scores (+5 bonus)
    curved_scores = list(map(lambda s: min(100, s + 5), scores))
    
    # Custom sorting by secondary tuple field
    employees = [("Rohan", 45000), ("Priya", 78000), ("Abhay", 65000)]
    sorted_by_salary = sorted(employees, key=lambda emp: emp[1], reverse=True)
    
    # Sum using reduce
    total_score = reduce(lambda acc, val: acc + val, scores)
    
    return passing_scores, curved_scores, sorted_by_salary, total_score


# ============================================================================
# 7. Recursion (Base Case + Recursive Step)
# ============================================================================
def factorial(n: int) -> int:
    """Calculates factorial recursively."""
    if n < 0:
        raise ValueError("Factorial undefined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


def is_palindrome_recursive(text: str) -> bool:
    """Recursively checks if string is a palindrome."""
    clean = "".join(ch.lower() for ch in text if ch.isalnum())
    if len(clean) <= 1:
        return True
    if clean[0] != clean[-1]:
        return False
    return is_palindrome_recursive(clean[1:-1])


# ============================================================================
# Execution & Demonstration Output
# ============================================================================
if __name__ == "__main__":
    print("--- 1. Basic Function & Tuple Unpacking ---")
    data = [12, 45, 7, 89, 34, 56]
    low, high, total, avg = calculate_metrics(data)
    print(f"Data: {data}")
    print(f"Min: {low}, Max: {high}, Sum: {total}, Avg: {avg}\n")

    print("--- 2. Positional vs Keyword vs Default Arguments ---")
    receipt1 = generate_receipt("Abhay Sharma", 2500)
    receipt2 = generate_receipt("Pooja Verma", 4000, discount=0.15, tax_rate=0.08)
    print("Receipt 1:", receipt1)
    print("Receipt 2:", receipt2, "\n")

    print("--- 3. Mutable Default Arguments Safety ---")
    list1 = add_item_safe("Laptop")
    list2 = add_item_safe("Mouse")
    print("List 1 (independent):", list1)
    print("List 2 (independent):", list2, "\n")

    print("--- 4. *args and **kwargs in Action ---")
    emp = build_employee_record(
        101, "Abhay",
        "AWS Certified", "Python Pro", "Scrum Master",
        department="Engineering", location="Pune", role="Data Analyst"
    )
    print("Employee Record:")
    for k, v in emp.items():
        print(f"  {k}: {v}")
    print()

    print("--- 5. Closures and nonlocal Scope ---")
    counter = outer_counter()
    print("Call 1:", counter())
    print("Call 2:", counter())
    print("Call 3:", counter(), "\n")

    print("--- 6. Lambdas, Map, Filter, Sorted ---")
    passed, curved, sorted_emps, total = functional_programming_demo()
    print(f"Passed: {passed}")
    print(f"Curved: {curved}")
    print(f"Sorted by Salary: {sorted_emps}")
    print(f"Total Sum: {total}\n")

    print("--- 7. Recursive Functions ---")
    print(f"Factorial of 6: {factorial(6)}")
    test_word = "A man a plan a canal Panama"
    print(f"Is '{test_word}' a palindrome? -> {is_palindrome_recursive(test_word)}")
