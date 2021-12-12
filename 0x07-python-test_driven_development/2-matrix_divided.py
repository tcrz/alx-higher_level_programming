#!/usr/bin/python3
"""
This is the 2-matrix_divided module
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix

    Args:
        matrix: list of lists of integers/floats
        div: integer or float value as the divisor

    Returns: new matrix with all elements of the matrix divided by div
    """
    length = 0
    new_matrix = []
    new_list = []
    typeerrormsg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(typeerrormsg)
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for each in matrix:
        if type(each) is not list:
            raise TypeError(typeerrormsg)
        if len(matrix[0]) != len(each):
            raise TypeError("Each row of the matrix must have the same size")
        for i in each:
            if type(i) is not int and type(i) is not float:
                raise TypeError(typeerrormsg)
        new_list = [round(n/div, 2) for n in each]
        new_matrix.append(new_list)
    return new_matrix
