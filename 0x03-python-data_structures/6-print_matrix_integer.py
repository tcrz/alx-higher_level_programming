#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    x = len(matrix)
    for i in range(x):
        for j in range(x):
            try:
                if j == x - 1:
                    print("{}".format(matrix[i][j]), end="")
                else:
                    print("{}".format(matrix[i][j]), end=" ")
            (except):
                print("", end="")
        print()
