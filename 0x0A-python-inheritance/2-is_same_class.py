#!/usr/bin/python3
"""
2-is_same_class module
"""


def is_same_class(obj, a_class):
    """
    returns True if object is exactly an instance of a specified class
    """
    return type(obj) is a_class
