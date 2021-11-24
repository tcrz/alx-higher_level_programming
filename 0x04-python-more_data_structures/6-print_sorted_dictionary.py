#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    order = sorted(a_dictionary.items())
    for k, v in order:
        print("{}: {}".format(k, v))
