#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = list(map(list, matrix))
    for i in range(len(new_matrix)):
        for n in range(len(new_matrix[i])):
            new_matrix[i][n] = new_matrix[i][n]**2
    return(new_matrix)
