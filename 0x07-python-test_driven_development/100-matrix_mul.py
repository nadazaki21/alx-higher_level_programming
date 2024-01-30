#!/usr/bin/python3
"""
Function that mutiplies  matrices
given that  the cinditions for multiplication are present
"""


def matrix_mul(m_a, m_b):
    """ mutiplies  matrices
given that  the cinditions for multiplication are present"""

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
                result_matrix = []
                for i in range(rows_a):  # Iterate over rows of matrix A
                    new_row = []  # Create a new row for the resulting matrix
                    for j in range(col_b):  # Iterate over columns of matrix B
                        dot_product = 0
                        for k in range(col_a):
                            dot_product += m_a[i][k] * m_b[k][j]
                        # Append the dot product to the new row
                        new_row.append(dot_product)
                    result_matrix.append(new_row)

            return result_matrix
