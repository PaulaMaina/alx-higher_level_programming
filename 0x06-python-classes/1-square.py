#!/usr/bin/python3
"""Square class definition with a private attribute size"""


class Square():
    """Definition of 'Square'"""
    def __init__(self, size=0):
        """Init an object of square with a private instance attribute 'size'

            Args:
                size: size of a square
        """
        self.__size = size
