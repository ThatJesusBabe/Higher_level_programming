#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for colunm in row:
             if colunm == row[-1]:
                print("{}".format(colunm), end = "")
             else:
                print('{:d}'.format(colunm), end=' ')
        print("")
