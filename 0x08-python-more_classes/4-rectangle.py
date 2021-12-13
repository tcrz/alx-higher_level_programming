#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """defines a Rect class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """perimeter for a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    def __repr__(self):
        """returns an “official” string representation of an instance"""
        values = '(' + str(self.__width) + ', ' + str(self.__height)
        rep = rep = 'Rectangle' + values + ')'
        return rep

    def __str__(self):
        """returns “informal” printable string representation of an instance"""
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return rec
        rec = "\n".join("#" * self.__width for i in range(self.__height))
        return rec
