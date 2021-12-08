#!/usr/bin/python3
"""Define a Class"""


class Square:
    """A Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    """method that returns area of a square"""
    def area(self):
        return (self.__size ** 2)

    """property to retrieve attribute, size"""
    @property
    def size(self):
        return self.__size

    """property to retrieve position attribute"""
    @property
    def position(self):
        return self.__position

    """property to set value for size attribute"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """property to set value for position attribute"""
    @position.setter
    def position(self, value):
        if value[0] < 0 or value[1] < 0:
            """Sets the position to a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    """method to print a square with position"""
    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__position[1]):
                print("")
            for j in range(self.__size):
                for y in range(self.__position[0]):
                    print(" ", end="")
                for x in range(self.__size):
                    print("#", end="")
                print("")
