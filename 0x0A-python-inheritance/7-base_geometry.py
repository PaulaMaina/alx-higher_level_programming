#!/usr/bin/python3
"""Defines a BaseGeometry Class"""


class BaseGeometry:
    """BaseGeometry class with an area method"""
    def area(self):
        """Raises an exception that it's not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

            Args:
                name: string
                value: value
            Raises:
                TypeError: if value is not an int
                ValueError: if value is <= 0
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
