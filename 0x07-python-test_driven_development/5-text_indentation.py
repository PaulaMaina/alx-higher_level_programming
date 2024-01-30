#!/usr/bin/python3
"""Text Indentation module"""


def text_indentation(text):
    """Prints a text with 2 new lines after . ? and :
        Args:
            text: Text to print
        Raises:
            TypeError: if text is not a string
    """
    first = 0
    ops = {".", "?", ":"}
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for last in range(len(text)):
        if text[last] in ops:
            line = text[first:last + 1] + "\n\n"
            first = last + 1
            print("{}".format(line.strip(" ")), end="")
    if first <= last:
        line = text[first:last + 1]
        print("{}".format(line.strip(" ")), end="")
