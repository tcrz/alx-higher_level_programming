#!/usr/bin/python3
"""
This is the 100-matrix_mul module
"""


def matrix_mul(m_a, m_b):
    """
    multiplies 2 matrices

    Args:
        m_a (list): list of lists
        m_b (list): list of lists

    Returns:
        list: a list of lists(matrix)
    """
    new_matrix = []
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for each in m_a:
        if type(each) is not list:
            raise TypeError("m_a must be a list of lists")
    for each in m_b:
        if type(each) is not list:
            raise TypeError("m_b must be a list of lists")
    if not m_a:
        raise TypeError("m_a can't be empty")
    for each in m_a:
        if not each:
            raise TypeError("m_a can't be empty")
    if not m_b:
        raise TypeError("m_b can't be empty")
    for each in m_b:
        if not each:
            raise TypeError("m_b can't be empty")
    for each in m_a:
        for i in each:
            if type(i) is not int and type(i) is not float:
                raise TypeError("m_a should contain only integers or floats")
    for each in m_b:
        for i in each:
            if type(i) is not int and type(i) is not float:
                raise TypeError("m_b should contain only integers or floats")
    for each in m_a:
        for i in each:
            if len(m_a[0]) != len(each):
                raise TypeError("each row of m_a must be of the same size")
    for each in m_b:
        for i in each:
            if len(m_b[0]) != len(each):
                raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = [[sum(i * j for i, j in zip(r, c)) for c in zip(*m_b)]
                  for r in m_a]
    return new_matrix
