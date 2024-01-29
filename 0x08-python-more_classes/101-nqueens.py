#!/usr/bin/python3
import sys


"""First element-column, second element-row"""
def reject(board):
    for col_1 in board:
        for col_2 in board:
            if not col_1 is col_2:
                if col_1[0] == col_2[0]:
                    return True
                if col_1[1] == col_2[1]:
                    return True
                if col_1[1] - col_1[0] == col_2[1] - col_2[0]:
                    return True
                if col_1[0] + col_1[1] == col_1[0] + col_2[1]:
                    return True
    return False
