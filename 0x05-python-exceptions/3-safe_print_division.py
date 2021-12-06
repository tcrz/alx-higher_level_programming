#!/usr/bin/python3
def safe_print_division(a, b):
    x = None
    try:
        print("Inside result: ", end="")
        x = a / b
    except (TypeError, ValueError, ZeroDivisionError):
        return (x)
    finally:
        print(x)
    return (x)
