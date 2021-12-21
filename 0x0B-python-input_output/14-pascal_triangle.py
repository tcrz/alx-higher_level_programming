#!/usr/bin/python3
"""
pascal's triangle
"""


def pascal_triangle(n):
    """
    Returns the pascal triangle of n.
    """

    if n <= 0:
        return []

    x = [[0 for x in range(i + 1)] for i in range(n)]
    x[0] = [1]

    for i in range(1, n):
        x[i][0] = 1
        for j in range(1, i + 1):
            if j < len(x[i - 1]):
                x[i][j] = x[i - 1][j - 1] + x[i - 1][j]
            else:
                x[i][j] = x[i - 1][0]
    return x
