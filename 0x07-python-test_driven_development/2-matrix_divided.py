#!/usr/bin/python3

"""This module will divide a matrix by an integer"""


def matrix_divided(matrix, div):
    """Plenty of logic stuff"""
    rowError = 'Each row of the matrix must have the same size'
    matError = 'matrix must be a matrix (list of lists) of integers/floats'
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    if type(matrix) != list:
        raise TypeError(matError)
    if div == 0:
        raise ZeroDivisionError('division by zero')
    newmatrix = list(map(list, matrix))
    for i in range(len(matrix)):
        if type(matrix[i]) == list:
            ogLen = len(matrix[0])
            for n in range(len(matrix[i])):
                if type(matrix[i][n]) not in [int, float]:
                    raise TypeError(matError)
                if len(matrix[i]) != ogLen:
                    raise TypeError(rowError)
                num = matrix[i][n] / div
                newmatrix[i][n] = float(round(num, 2))
        else:
            raise TypeError(matError)
    return newmatrix
