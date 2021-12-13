#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """defines a Rect class"""
    def __init__(self, height, width):
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.width

    @width.setter
    def width(self, width):
        """width setter"""
        if not isinstance(width, int) and not isinstance(width, float):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width

    @property
    def height(self):
        """height getter"""
        return self.height

    @height.setter
    def height(self, height):
        """height setter"""
        if not isinstance(height, int) and not isinstance(height, float):
            raise TypeError("width must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.height = height
