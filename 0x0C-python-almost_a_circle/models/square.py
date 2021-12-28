#!/bin/usr/python3
"""
Square class module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialises square object with given atrributes"""
        super().__init__(x=x, y=y, id=id, width=size, height=size)

    def __str__(self):
        """returns string output"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
