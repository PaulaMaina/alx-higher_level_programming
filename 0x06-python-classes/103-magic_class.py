#!/usr/bin/python3
"""Definition of 'MagicClass' that matches the bytecode provided"""

import math


class MagicClass:
    """Represents a circle"""

    def __init__(self, radius=0):
        """Initiates MagiClass

            Args:
                radius: radius of a MagicClass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Returns the area of a circle"""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Returns the circumference of a circle"""
        return (2 * math.pi * self.__radius)
