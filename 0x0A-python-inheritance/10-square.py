#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Square Class
"""


class Square(Rectangle):
    """defines a square class"""

    def __init__(self, size):
        """initializes square instance"""
        self.__size = size
        integer_validator("size", size)

    def area(self):
        """area of a square obj"""
        return self.__size ** 2
