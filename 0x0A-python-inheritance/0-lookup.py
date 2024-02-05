#!/usr/bin/python3
"""Lookup module"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object

        Args:
            obj: object
        Returns:
            A list object
    """
    return dir(obj)
