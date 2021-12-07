#!/usr/bin/python3
"""
Define a Square class
"""


class Square:
    """A class that defines a Square with a private attribute called size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """A public instance method that returens the current square area"""
    def area(self):
        return (self.__size ** 2)
