#!/usr/bin/python3
"""
This is the 3-say_my_name.py module
"""


def say_my_name(first_name, last_name=""):
    """
    prints My name is <first name> <last name>

    Args:
        first_name (str): str argument
        last_name (str, optional): str argument. Defaults to "".
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if type(first_name) is str and type(last_name) is str:
        print("My name is {} {}".format(first_name, last_name))
