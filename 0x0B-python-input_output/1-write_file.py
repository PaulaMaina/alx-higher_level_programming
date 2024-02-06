#!/usr/bin/python3
"""Write file module"""


def write_file(filename="", text=""):
    """Writes a string to a text file

        Args:
            filename: The name of  file
            text: string to be written to the file
        Returns:
            The number of characters written
    """
    characters = 0
    with open(filename, "r", encoding="utf-8") as f:
        while f.readline() != "":
            characters += 1
    return characters
