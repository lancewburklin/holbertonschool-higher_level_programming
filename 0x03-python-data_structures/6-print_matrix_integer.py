#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    flag = False
    if matrix:
        for i in range(len(matrix)):
            elend = " "
            for x in range(len(matrix[i])):
                if x == len(matrix[i]) - 1:
                    elend = "\n"
                print("{:d}".format(matrix[i][x]), end=elend)
                flag = True
    if flag == False:
        print("")
