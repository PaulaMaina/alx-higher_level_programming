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
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
    return 0
