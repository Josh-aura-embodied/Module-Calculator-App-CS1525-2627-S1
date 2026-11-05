"""Main program for the interactive calculator."""

from operations import add, subtract, multiply, divide
from utils import get_user_number, get_operation


def main():
    print("Interactive Calculator")
    print("----------------------")

    number_one = get_user_number("Enter your first number: ")
    number_two = get_user_number("Enter your second number: ")
    operation = get_operation()

    while operation == "/" and number_two == 0:
        print("You cannot divide by zero. Please enter another number.")
        number_two = get_user_number("Enter your second number: ")

    if operation == "+":
        result = add(number_one, number_two)
    elif operation == "-":
        result = subtract(number_one, number_two)
    elif operation == "*":
        result = multiply(number_one, number_two)
    else:
        result = divide(number_one, number_two)

    print("----------------------")
    print(f"Result: {number_one} {operation} {number_two} = {result}")


if __name__ == "__main__":
    main()