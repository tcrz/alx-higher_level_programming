#!/usr/bin/python3
"""find peak in a  list of unsorted integers"""


def find_peak(list_of_integers):
    """function to find peak"""
    num = 0
    if len(list_of_integers) == 0:
        return None
    else:
        for i in list_of_integers:
            if i > num:
                num = i
        return num
