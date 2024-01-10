#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_new = []
    for i in matrix:
        i_new = list(map((lambda x: x**2), i))
        matrix_new.append(i_new)
    return matrix_new
