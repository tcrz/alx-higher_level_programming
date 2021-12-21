#!/usr/bin/python3
"""
Square Class
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a square class"""

    def __init__(self, size):
        """initializes square instance"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of a square obj"""
        return self.__size ** 2

    def __str__(self):
        """return string format of area for Rectangle obj"""
        return str("[Square] {}/{}".format(self.__size, self.__size))
