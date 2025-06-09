"""Basic arithmetic utility functions."""

def add(a: int, b: int) -> int:
    """Return the sum of a and b."""
    return a + b

def sub(a: int, b: int) -> int:
    """Return the difference of a and b."""
    return a - b

def mult(a: int, b: int) -> int:
    """Return the product of a and b."""
    return a * b

def div(a: int, b: int) -> float:
    """Return the quotient of a divided by b."""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b