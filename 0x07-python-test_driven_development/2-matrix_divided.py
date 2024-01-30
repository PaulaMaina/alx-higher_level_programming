#!/usr/bin/python3
"""Matrix divided module"""


def matrix_divided(matrix, div):
    """Division of matrix elements

        Args:
            matrix: a list of lists of ints or floats
            div: The divisor
        Raises:
            TypeError: if the matrix is not a list of lists or
                the rows of the matrix  are not of equal size or
                div is not an int or float
            ZeroDivisionError: if div is 0
        Returns:
            The new matrix containing quotients
    """
    msg = "matrix must be a matrix(list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_length = None
    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(msg)
        if row_length is not None and row_length != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        row_length = len(row)
        for col in row:
            if not isinstance(col, int) and not isinstance(col, float):
                raise TypeError(msg)

    return [[round(col / div, 2) for col in row] for row in matrix]
