#!/usr/bin/python3
"""Same class module"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the specified class

        Args:
            obj: object
            a_class: class that the object is an instance of
        Returns:
            True if object is an instance of a_class, otherwise false

    """
    return type(obj) == a_class
