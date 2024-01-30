#!/usr/bin/python3
"""
lazy matrix mutiplication
using built in function from numpy
"""

import numpy as np   # as is for aliasing gthe module name


def lazy_matrix_mul(m_a, m_b):
    """
    producing the product of the matrix, but using the numpy module
    not the manual way as previous

    """
    # checking if matrix is a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # checking if matrix is a list of lists
    for inner_list in m_a:
        if not isinstance(inner_list, list):
            raise TypeError("m_a must be a list of lists")

    for inner_list in m_b:
        if not isinstance(inner_list, list):
            raise TypeError("m_b must be a list of lists")

    # checking if matrix is empty
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    elif len(m_a) != 0 and len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    elif len(m_b) != 0 and len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    # checking if all elements of the matrix are ineteers or float

    for inner_list in m_a:
        for i in inner_list:
            if not isinstance(i, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for inner_list in m_b:
        for i in inner_list:
            if not isinstance(i, (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    # checking if row lenght in matices is consistant
        # for matrix a
            rows_a = 1
            col_a = 0
            first_len = len(m_a[0])
            col_a = first_len
            for inner_list in m_a[1:]:
                if len(inner_list) != first_len:
                    raise TypeError("each row of m_a must be of the same size")
                else:
                    rows_a = rows_a + 1

            # for matrix b
            rows_b = 1
            col_b = 0
            first_len = len(m_b[0])
            col_b = first_len
            for inner_list in m_b[1:]:
                if len(inner_list) != first_len:
                    raise TypeError("each row of m_b must be of the same size")
                else:
                    rows_b = rows_b + 1

            # checking if the 2 matrices can be mutiplied or not
            if col_a != rows_b:
                raise ValueError("m_a and m_b can't be multiplied")
            else:
                matrix_a = np.array(m_a)
                matrix_b = np.array(m_b)

                result_dot = np.dot(matrix_a, matrix_b)
            return result_dot
