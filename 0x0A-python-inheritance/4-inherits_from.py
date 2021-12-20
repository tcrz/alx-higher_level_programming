#!/usr/bin/python3
"""
4-inherits_from module
"""


def inherits_from(obj, a_class):
    """
    returns True if the object is an instance of a classthat
    inherited (directly or indirectly) from  the specified class ;
    otherwise False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
