#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for k, v in list(a_dictionary.items()):
        if v == value:
            del a_dictionary[k]
    return a_dictionary
