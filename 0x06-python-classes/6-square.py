#!/usr/bin/python3
"""Define a Class"""


class Square:
    """A Square Class"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def area(self):
        """method that returns area of a square"""
        return (self.__size ** 2)

    @property
    def size(self):
        """property to retrieve attribute, size"""
        return self.__size

    @property
    def position(self):
        """property to retrieve position attribute"""
        return self.__position

    @size.setter
    def size(self, value):
        """property to set value for size attribute"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """property to set value for position attribute"""
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def my_print(self):
        """method to print a square with position"""
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
