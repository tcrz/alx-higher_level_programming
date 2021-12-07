#!/usr/bin/python3
"""Define a Class"""


class Square:
    """A Square Class"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    """property to retrieve attribute, size"""
    @property
    def size(self):
        return self.__size

    """property to set value for size attribute"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        for i in range(self.__size):
            for x in range(self.__size):
                print("#", end="")
            print("")
