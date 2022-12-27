#!/usr/bin/python3
"""
No module imported
"""


def matrix_divided(matrix, div):
    """
    method that defines new matrix after all elements are divided
    """

    new_matrix = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        transpose = []
        for elements in row:
            if type(elements) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")
            elements = round(elements / div, 2)
            transpose.append(elements)
        new_matrix.append(transpose)
    return new_matrix
