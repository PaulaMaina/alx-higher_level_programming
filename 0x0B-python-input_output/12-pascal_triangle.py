#!/usr/bin/python3
"""Pascal triangle module"""

def pascal_triangle(n):
    """Returns a 2D list representing the Pascal's triangle"""
    pascal = []
    previous = [1]

    if n > 0:
        pascal.append(previous)
        previous = previous.copy()
    for x in range(1, n):
        for y in range(len(previous[1:])):
            previous[y] += previous[1:][y]
        previous.insert(0, 1)
        pascal.append(previous)
        previous = previous.copy()

    return pascal
