#!/usr/bin/python3
"""Defines a Student Class"""


class Student:
    """A student class with attribute"""
    def __init__(self, first_name, last_name, age):
        """Initiates object attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves the dictionary representation of an instance"""
        my_dict = {}
        if isinstance(attrs, list):
            for name in attrs:
                if isinstance(name, str) and name in self.__dict__:
                    my_dict[name] = self.__dict__[name]
            return my_dict
        return self.__dict__
