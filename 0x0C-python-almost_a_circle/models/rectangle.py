#!/usr/bin/python3
"""
Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """defines a rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initialise rectangle object"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x setter"""
        return self.__x

    @property
    def y(self):
        """y setter"""
        return self.__y

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of a rectangle"""
        return self.__height * self.__width

    def display(self):
        """prints rectanglel instance with '#' """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(end=" ")
            for x in range(self.__width):
                print('#', end="")
            print()

    def __str__(self):
        """returns given string output"""
        return str("[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        # attrs = [self.id, self.width, self.height, self.x, self.y]
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
            # --------------------------------
            # kd = {'id': 'id', 'width': '_Rectangle__width',
            #        'height': '_Rectangle__height',
            #        'x': '_Rectangle__x', 'y': '_Rectangle__y'}
            # list_attr = list(self.__dict__)
            # for k, v in kwargs.items():
            #     self.__dict__[kd[k]] = v
            # ------------------------------
            # x = len(kwargs)
            # list_attrs = list(self.__dict__)
            # for i in range(len(list_attrs)):
            #     for k, v in kwargs.items():
            #         if k == list_attrs[i][12:] or k == list_attrs[i]:
            #             setattr(self, list_attrs[i], v)
