#!/usr/bin/python3
"""
2-append_write module
"""


def append_write(filename="", text=""):
    """
    appends a string to a text file and
    returns the number of characters written
    """

    with open(filename, mode='a', encoding='utf-8') as file:
        return(file.write(text))
