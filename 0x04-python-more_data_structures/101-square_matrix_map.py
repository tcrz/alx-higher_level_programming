#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    new_list = []
    for eachlist in matrix:
        new_list.append(list(map(lambda x: x * x, eachlist)))
    return new_list
