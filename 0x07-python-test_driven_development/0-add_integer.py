#!/usr/bin/python3
"""
This is the 0-add_integer module
"""


def add_integer(a, b=98):
    """
    returns the sum of two integers

    Args:
        a (int): integer value
        b (int, optional): integer value. Defaults to 98.

    Returns:
        int: Sum of a and b
    """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
