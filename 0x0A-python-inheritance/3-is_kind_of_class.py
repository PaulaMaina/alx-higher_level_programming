#!/usr/bin/python3
"""Object class module"""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of or
    an instance of a class that is a child of specified class 

        Args:
            obj: object
            a_class: class that the object is an instance of
        Returns:
            True if object is an instance of a_class, otherwise false

    """
    return isinstance(obj, a_class)
