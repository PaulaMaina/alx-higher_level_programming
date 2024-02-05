#!/usr/bin/python3
"""Defines a BaseGeometry Class"""


class BaseGeometry:
    """BaseGeometry class with an area method"""
    def area(self):
        """Raises an exception that it's not implemented"""
        raise Exception("area() is not implemented")
