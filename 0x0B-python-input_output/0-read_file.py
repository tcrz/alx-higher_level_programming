#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """reads a texts file and prints it to stdout"""

    with open(filename, mode='r', encoding='utf-8') as file:
        print(file.read(), end="")
