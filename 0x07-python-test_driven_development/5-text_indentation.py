#!/usr/bin/python3
"""Text Indentation module"""


def text_indentation(text):
    """Prints a text with 2 new lines after . ? and :"""
    last = " "
    word = ""
    ops = [".", "?", ":"]
    if text == "":
        print(word, end="")
    if type(text) is not str:
        raise TypeError("text must be a string")
    for s in text:
        if s is last and s == " ":
            last = s
            continue
        is last in ops and s == " ":
            last = s
            continue
        word += s + "\n" + "\n" if s in ops else s
    print(word.rstrip(" "), end="")
