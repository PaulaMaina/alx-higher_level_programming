#!/usr/bin/python3
"""Defines a Rectangle Class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initiates a Rectangle class"""
    def __init__(self, width, height):
        """Validates and sets the private attributes width and height"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
