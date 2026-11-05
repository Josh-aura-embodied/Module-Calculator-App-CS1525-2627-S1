"""Basic calculator operations."""


def add(number_one: float, number_two: float) -> float:
    """Return the sum of two numbers."""
    return number_one + number_two


def subtract(number_one: float, number_two: float) -> float:
    """Return the difference between two numbers."""
    return number_one - number_two


def multiply(number_one: float, number_two: float) -> float:
    """Return the product of two numbers."""
    return number_one * number_two


def divide(number_one: float, number_two: float) -> float:
    """Return the result of dividing the first number by the second."""
    if number_two == 0:
        raise ValueError("Cannot divide by zero.")
    return number_one / number_two