"""Functions for collecting and checking calculator input."""


def get_user_number(prompt: str) -> float:
    """Ask for a number until the user enters a valid numeric value."""
    while True:
        user_input = input(prompt).strip()

        try:
            return float(user_input)
        except ValueError:
            print("Please enter a valid number.")


def get_operation() -> str:
    """Ask for a supported operation and return its symbol."""
    valid_operations = ("+", "-", "*", "/")

    while True:
        operation = input("Choose an operation (+, -, *, /): ").strip()

        if operation in valid_operations:
            return operation

        print("Invalid operation. Please choose +, -, *, or /.")