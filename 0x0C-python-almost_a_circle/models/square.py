#!/bin/usr/python3
"""
Square class module
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initialises square object with given atrributes"""
        self.size = size
        super().__init__(size, size, x, y, id)
        # super().__init__(x=x, y=y, id=id, width=size, height=size)

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

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute via *args or **kwargs"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif kwargs:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "size":
                    self.size = v
                if k == "x":
                    self.x = v
                if k == "y":
                    self.y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle Object"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
