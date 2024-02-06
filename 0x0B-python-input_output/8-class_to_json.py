#!/usr/bin/python3
"""Class to JSON module"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure

        Args:
            obj: instance of a class
        Returns:
            A dictionary description with simple data structure
    """
    return obj.__dict__
