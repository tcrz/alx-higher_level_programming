#!/usr/bin/python3
"""
7-base_geometry module
"""


class BaseGeometry:
    """BaseGeometry Class"""
    def area(self):
        """area method raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
