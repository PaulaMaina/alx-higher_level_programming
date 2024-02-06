#!/usr/bin/python3
"""Append write module"""


def append_write(filename="", text=""):
    """Appends a string at the text file

        Args:
            filename: The name of the file
            text: string to be append
        Returns:
            The number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
    return 0
