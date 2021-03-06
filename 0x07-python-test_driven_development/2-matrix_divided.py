#!/usr/bin/python3
"""Module for matrix_divided function"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix
    Args:
        matrix(int):matrix
        div(int, float):integer dividing elements
    Raises:
        TypeError: if matrix item is not integer or float
        TypeError: if rows of matrix is not same size
        TypeError: if div not float or integer
        ZeroDivisionError: if div  eequal to zero
    Returns:
        A new matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if not div:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    new_nums = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError('Each row of the matrix must have the same size')
        if not all(row) and all(matrix[row]) is False:
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        for num in row:
            if isinstance(num, (int, float)) is False:
                raise TypeError("matrix must be a matrix "
                                "(list of lists) of integers/floats")
            new_nums.append(round(num / div, 2))
        new_matrix.append(new_nums)
        new_nums = []
    return new_matrix
