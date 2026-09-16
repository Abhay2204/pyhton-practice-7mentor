"""
Module 14: Python Functions Practice Workbook
--------------------------------------------
Hands-on exercises covering function definitions, parameters, return values,
*args, **kwargs, recursion, lambdas, and modular program structure.
"""

import math

# ============================================================================
# 1. GEOMETRY & FORMULA FUNCTIONS
# ============================================================================
def circle_properties(radius: float):
    """Returns the area and circumference of a circle."""
    area = math.pi * (radius ** 2)
    circumference = 2 * math.pi * radius
    return round(area, 2), round(circumference, 2)

c_area, c_circ = circle_properties(7)
print(f"[1. Geometry] Radius: 7 -> Area: {c_area}, Circumference: {c_circ}")


# ============================================================================
# 2. TEMPERATURE CONVERTER WITH DEFAULT ARGUMENTS
# ============================================================================
def convert_temperature(temp: float, from_unit: str = "C", to_unit: str = "F") -> float:
    """Converts temperatures between Celsius, Fahrenheit, and Kelvin."""
    from_u = from_unit.upper()
    to_u = to_unit.upper()
    
    # First normalize to Celsius
    if from_u == "C":
        celsius = temp
    elif from_u == "F":
        celsius = (temp - 32) * 5 / 9
    elif from_u == "K":
        celsius = temp - 273.15
    else:
        raise ValueError(f"Unknown source unit: {from_unit}")

    # Convert Celsius to destination
    if to_u == "C":
        return round(celsius, 2)
    elif to_u == "F":
        return round((celsius * 9 / 5) + 32, 2)
    elif to_u == "K":
        return round(celsius + 273.15, 2)
    else:
        raise ValueError(f"Unknown destination unit: {to_unit}")

print(f"[2. Temp] 100 C -> F: {convert_temperature(100, 'C', 'F')}")
print(f"[2. Temp] 32 F -> C: {convert_temperature(32, 'F', 'C')}")
print(f"[2. Temp] 0 C -> K: {convert_temperature(0, 'C', 'K')}")


# ============================================================================
# 3. VARIABLE-LENGTH ARBITRARY MULTIPLICATION (*args)
# ============================================================================
def multiply_all(*numbers: float) -> float:
    """Multiplies all supplied numbers together. Returns 1 if none provided."""
    result = 1.0
    for num in numbers:
        result *= num
    return result

print(f"[3. *args] Product of (2, 3, 4, 5): {multiply_all(2, 3, 4, 5)}")
print(f"[3. *args] Product of (10, 20): {multiply_all(10, 20)}")


# ============================================================================
# 4. STUDENT REPORT GENERATOR (**kwargs)
# ============================================================================
def generate_report_card(student_name: str, student_class: str, **subject_marks):
    """Formats student details and calculates total and percentage."""
    total_marks = sum(subject_marks.values())
    subject_count = len(subject_marks)
    percentage = (total_marks / (subject_count * 100)) * 100 if subject_count > 0 else 0
    grade = "A+" if percentage >= 90 else "A" if percentage >= 75 else "B" if percentage >= 50 else "C"

    return {
        "Student": student_name,
        "Class": student_class,
        "Marks": subject_marks,
        "Total": f"{total_marks} / {subject_count * 100}",
        "Percentage": f"{percentage:.2f}%",
        "Grade": grade,
    }

card = generate_report_card(
    "Abhay", "12th Science",
    Physics=88, Chemistry=92, Mathematics=95, English=85
)
print("[4. **kwargs] Report Card:")
for k, v in card.items():
    print(f"   {k}: {v}")


# ============================================================================
# 5. RECURSIVE EXPONENTIATION (x^n)
# ============================================================================
def power_recursive(base: float, exponent: int) -> float:
    """Computes base^exponent recursively."""
    if exponent == 0:
        return 1
    if exponent < 0:
        return 1 / power_recursive(base, -exponent)
    return base * power_recursive(base, exponent - 1)

print(f"[5. Recursion] 2^8 = {power_recursive(2, 8)}")
print(f"[5. Recursion] 5^-2 = {power_recursive(5, -2)}")


# ============================================================================
# 6. HIGHER-ORDER & LAMBDA TRANSFORMATIONS
# ============================================================================
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even squares using filter and map
even_squares = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(f"[6. Lambdas] Even squares from 1..10: {even_squares}")

# Sorting tuples by multiple criteria
products = [
    {"name": "Laptop", "price": 55000, "rating": 4.5},
    {"name": "Mouse", "price": 800, "rating": 4.8},
    {"name": "Monitor", "price": 14000, "rating": 4.2},
    {"name": "Keyboard", "price": 2500, "rating": 4.6},
]
by_rating = sorted(products, key=lambda p: p["rating"], reverse=True)
print(f"[6. Lambdas] Best rated item: {by_rating[0]['name']} ({by_rating[0]['rating']} stars)")
