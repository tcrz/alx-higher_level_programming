#!/usr/bin/python3
"""
Rectangle Class module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines a rectangle Class"""

    def __init__(self, width, height):
        """initializes an instance of the defined class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
