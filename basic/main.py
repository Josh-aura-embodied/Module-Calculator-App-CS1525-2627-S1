"""Main program for the basic calculator."""

from operations import add, subtract, multiply, divide


def main():
    number_one = 12
    number_two = 4

    print("Basic Calculator")
    print("----------------")

    print(f"{number_one} + {number_two} = {add(number_one, number_two)}")
    print(f"{number_one} - {number_two} = {subtract(number_one, number_two)}")
    print(f"{number_one} * {number_two} = {multiply(number_one, number_two)}")
    print(f"{number_one} / {number_two} = {divide(number_one, number_two)}")


if __name__ == "__main__":
    main()