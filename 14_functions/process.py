"""
Arithmetic Operations Module
Provides pure calculation functions with error handling.
"""

def add(a: float, b: float) -> float:
    """Returns the sum of a and b."""
    return a + b

def sub(a: float, b: float) -> float:
    """Returns the difference of a and b."""
    return a - b

def multiplication(a: float, b: float) -> float:
    """Returns the product of a and b."""
    return a * b

def division(a: float, b: float):
    """Returns the quotient of a and b or an error message if b is zero."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulus(a: float, b: float):
    """Returns the remainder of a divided by b."""
    if b == 0:
        return "Cannot divide by zero"
    return a % b

def power(a: float, b: float) -> float:
    """Returns a raised to power b."""
    return a ** b
