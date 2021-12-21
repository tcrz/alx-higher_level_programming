#!/usr/bin/python3
"""
1-write_file module
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file and
    returns the number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return (file.write(text))
