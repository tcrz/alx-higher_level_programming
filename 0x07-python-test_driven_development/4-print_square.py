#!/usr/bin/python3
"""
This is the 4-print_square module
"""


def print_square(size):
    """prints a square with the character #.

    Args:
        size (int): size length of the square
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for x in range(size):
            print("#", end="")
        print()
