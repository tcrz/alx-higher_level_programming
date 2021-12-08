#!/usr/bin/python3
"""Define a Class"""


class Square:
    def __init__(self, size=0):
        """initialization of Square"""
        self.size = size

    @property
    def size(self):
        """getter method"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method for size attribute"""
        if type(value) is not int:
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """method that returns square area of a Square"""
        return (self.__size ** 2)

    def __eq__(self, self2):
        """checks if equals"""
        return self.size == self2.size

    def __ne__(self, self2):
        """checks if not equal"""
        return self.size != self2.size

    def __le__(self, self2):
        """checks if less than or equal"""
        return self.size <= self2.size

    def __ge__(self, self2):
        """checks if greater than or equal"""
        return self.size >= self2.size

    def __lt__(self, self2):
        """checks if less than"""
        return self.size < self2.size

    def __gt__(self, self2):
        """checksk if greater than"""
        return self.size > self2.size
