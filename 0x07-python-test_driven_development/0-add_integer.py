#!/usr/bin/python3
"""Add integers module"""


def add_integer(a, b=98):
    """Add two integers
        Args:
            a: first integer
            b: second integer
        Raises:
            TypeError: if a or b is not an int or float
        Returns:
            Sum of a and b
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
