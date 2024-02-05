#!/usr/bin/python3
"""MyList subclass"""


class MyList(list):
    """Subclass of List class"""

    def print_sorted(self):
        """Prints a list sorted in ascending order"""
        print(sorted(self))
