#!/usr/bin/python3
"""Define a Class"""


class Square:
    def __init__(self, size=0):
        """initialization of Square"""
        self.__size = size

    @property
    def size(self):
        """getter method"""
        return self.size

    @size.setter
    def size(self, value):
        """setter method for size attribute"""
        if value < 0:
            ValueError("size must be >= 0")
        elif type(value) is not int:
            TypeError("size must be a number")
        else:
            self.__size = value

    def area(self):
        """method that returns square area of a Square"""
        return (self.__size ** 2)

    def __eq__(self, self2):
        """checks if equals"""
        return self.__size == self2.__size

    def __ne__(self, self2):
        """checks if not equal"""
        return self.__size != self2.__size

    def __le__(self, self2):
        """checks if less than or equal"""
        return self.__size <= self2.__size

    def __ge__(self, self2):
        """checks if greater than or equal"""
        return self.__size >= self2.__size

    def __lt__(self, self2):
        """checks if less than"""
        return self.__size < self2.__size

    def __gt__(self, self2):
        """checksk if greater than"""
        return self.__size > self2.__size
