#!/usr/bin/python3
"""Defines a LockedClass"""


class LockedClass:
    """An empty class that only allows the first_name attr"""
    __slots__ = ["first_name"]
