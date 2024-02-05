#!/usr/bin/python3
"""Object class module"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a_class
        Args:
            obj: object
            a_class: class that the object is an instance of
        Returns:
            True if object inherits, otherwise false

    """
    return isinstance(obj, a_class) and type(obj) is not a_class
