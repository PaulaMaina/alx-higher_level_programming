#!/usr/bin/python3
"""Defines an add_attribute function"""


def add_attribute(obj, name, value):
    """Adds an attribute to an object

        Args:
            obj: object
            name: name of the attribute
            value: value of the attribute
        Raises:
            TypeError: if the attribute cannot be added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
