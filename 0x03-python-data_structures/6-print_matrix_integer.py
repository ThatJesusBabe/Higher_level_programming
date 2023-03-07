#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for colunm in row:
            print("{:d}".format(colunm), end = " ")
        print("")
