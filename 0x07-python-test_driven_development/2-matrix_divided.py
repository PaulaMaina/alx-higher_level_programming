#!/usr/bin/python3
"""Matrix divided module"""


def matrix_divided(matrix, div):
    """Division of matrix elements"""
    msg = "matrix must be a matrix(list of lists) of integers/floats"
    new_mat = []

    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(msg)
    if type(div) is not int and type(div) is not float and div is not None:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix[0]:
        size = len(matrix[0])
    else:
        raise TypeError(msg)
    for x in range(len(matrix)):
        if len(matrix[x]) != size:
            raise TypeError("Each row of the matrix must have the same size")
        new_mat.append([])
        for y in matrix[x]:
            if type(y) is int or type(y) is float:
                new_mat[x].append(round(y / div, 2))
            else:
                raise TypeError(msg)

    return new_mat
