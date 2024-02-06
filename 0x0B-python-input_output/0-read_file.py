#!/usr/bin/python3
"""Read file module"""


def read_file(filename=""):
    """Prints the content of the text file

        Args:
            filename: The name and path of the file
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
