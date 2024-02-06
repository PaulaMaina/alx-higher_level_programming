#!/usr/bin/python3
"""Defines a Student Class"""


class Student:
    """A student class with attribute"""
    def __init__(self, first_name, last_name, age):
        """Initiates object attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves the dictionary representation of an instance"""
        return self.__dict__
