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

    def integer_validator(self, name, value):
        """validates attributes"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if name == 'x' or name == 'y':
            if value < 0:
                raise ValueError("{} must be >= 0".format(name))
        else:
            if value <= 0:
                raise ValueError("{} must be > 0".format(name))
