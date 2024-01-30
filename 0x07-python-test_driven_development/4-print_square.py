#!/usr/bin/python3


def print_square(size):
    """Print square function
        Args:
            size: Size of the square
        Raises:
            TypeError: size is not an int
            ValueError: size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print("{}".format(("#" * size + "\n") * size), end="")
