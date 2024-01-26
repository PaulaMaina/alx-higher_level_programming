#!/usr/bin/python3
"""Name printing module"""


def say_my_name(first_name, last_name=""):
    """Prints the first and last name"""
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print(f"My ma,e is {first_name}", end="")
    if len(last_name) == 0:
        print()
    else:
        print(f" {last_name}")
