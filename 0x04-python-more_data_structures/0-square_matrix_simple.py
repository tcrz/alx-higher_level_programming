#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newlist = []
    for eachlist in matrix:
        newlist.append(list(map(lambda a: a * a, eachlist)))
    return newlist
