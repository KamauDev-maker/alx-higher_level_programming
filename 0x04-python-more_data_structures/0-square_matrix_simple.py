#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_list = []
    for x in matrix:
        new_list.append(list(map(lambda x: x**2, x)))
    return (new_list)
