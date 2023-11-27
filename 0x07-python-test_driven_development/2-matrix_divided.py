#!/usr/bin/python3

"""This function defines a matrix division"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): The input matrix (list of lists of integers or floats).
        div (int or float): The divisor.

    Returns:
        A new matrix representing the result of the division.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   or if each row of the matrix has different sizes,
                   or if div is not a number (integer or float).
        ZeroDivisionError: If the divisor =  0.
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
