#!/usr/bin/python3
def safe_print_division(a, b):
    x = None
    try:
        print("Inside result: ", end="")
        x = a / b
        print(x)
    except ZeroDivisionError:
        print(x)
    finally:
        return x
