#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Rectangle Class
"""


class Rectangle(BaseGeometry):
    """defines a rectangle Class"""

    def __init__(self, width, height):
        """initializes an instance of the defined class"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """returns the area of a Rectangle obj"""
        return self.__width * self.__height

    def __str__(self):
        """return string format of area for Rectangle obj"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
