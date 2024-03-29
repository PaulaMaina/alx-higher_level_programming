#!/usr/bin/python3
"""Defines a Square Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A subclass of Rectangle"""
    def __init__(self, size):
        """Initiates the width and height to size"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns a string description of the square"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
