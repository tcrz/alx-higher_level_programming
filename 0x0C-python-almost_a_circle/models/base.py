#!/usr/bin/python3
"""
Base Class
"""


class Base:
    """defining base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialises instance of a Base class"""
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base. __nb_objects
