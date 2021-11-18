#!/usr/bin/python
import sys
from calculator_1 import add, sub, mul, div


def calc(func, a, b, sign):
    c = func(a, b)
    print("{:d} {} {:d} = {:d}".format(a, sign, b, c))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if sys.argv[2] == '+':
        calc(add, a, b, '+')
    elif sys.argv[2] == '-':
        calc(sub, a, b, '-')
    elif sys.argv[2] == '*':
        calc(mul, a, b, '*')
    elif sys.argv[2] == '/':
        calc(div, a, b, '/')
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
