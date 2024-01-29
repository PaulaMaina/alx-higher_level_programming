#!/usr/bin/python3
"""Empty rectangle class"""


class Rectangle():
    """Initializes a Rectangle object"""
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Width of a rectangle"""
        return self.__width

    @property
    def height(self):
        """Height of a rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """Assigns a value to width

            Args:
                value: value assigned to width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Assigns a value to height

            Args:
                value: value to be assigned to height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
