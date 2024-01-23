#!/usr/bin/python3
"""Square class definition with a private attribute size"""


class Square():
    """Definition of 'Square'"""
    def __init__(self, size=0):
        """Init an object of square with a private instance attribute 'size'

            Args:
                size: size of a square

            Raises:
            TypeError: Size is not an integer
            ValueError: Size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
