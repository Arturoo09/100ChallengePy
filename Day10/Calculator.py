import os
import platform
from Calculator_art import logo

print(f"{logo}\n")


def clear_screen():
    current_os = platform.system()
    if current_os == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Funciones


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculator_func():

    num1 = float(input("What's the first number??: "))

    for key in operations:
        print(f"{key}")

    exit_calculator = False

    while not exit_calculator:
        operator = input("Pick a operation from above: ")

        num2 = float(input("What's the second number??: "))

        calculator = operations[operator]
        result = calculator(num1, num2)

        print(f"{num1} {operator} {num2} = {result}")

        flag = input(
            f"Do you want to continue calculating with {result} (Y/N): ")
        if flag == "N":
            exit_calculator = True
            clear_screen()
        else:
            num1 = result


calculator_func()
