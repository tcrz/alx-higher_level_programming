#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum_of_tuples = ()
    ntuple_a = tuple_a + (0, 0)
    ntuple_b = tuple_b + (0, 0)
    sum_of_tuples = ntuple_a[0] + ntuple_b[0], ntuple_b[1] + ntuple_a[1]
    return sum_of_tuples
