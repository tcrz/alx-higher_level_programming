#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v == 0:
                max = v
            if max < v:
                max = v
                key = k
        return key
