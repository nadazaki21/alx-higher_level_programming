#!/usr/bin/python3
"""
 function that divides all elements of a matrix

"""


def matrix_divided(matrix, div):
    first_len = len(matrix[0])
    for inner_list in matrix:
        if len(inner_list) != first_len:
            raise TypeError("Each row of the matrix must have the same size")
        for i in inner_list:   # check that all are ints or floats
            if not isinstance(i, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)"
                    " of integers/floats"
                    )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new_matrix = []
        for inner_list in matrix:
            new_inner_list = []
            for i in inner_list:
                new_inner_list.append(round((i / div), 2))
            new_matrix.append(new_inner_list)

        return new_matrix
