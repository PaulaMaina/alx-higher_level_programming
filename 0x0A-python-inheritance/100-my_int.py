#!/usr/bin/python3
"""Defines a MyInt Class"""

class MyInt(int):
    """Inverts == and !="""
    def __eq__(self, other):
        """Returns self != other"""
        return bool(self - other)

    def __ne__(self, other):
        """Returns self == other"""
        return not bool(self - other)
