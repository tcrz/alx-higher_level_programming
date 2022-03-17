#!/usr/bin/python3
"""find peak in a  list of unsorted integers"""


def find_peak(list_of_integers):
    """function to find peak"""
    if list_of_integers:
        num = 0
        for i in list_of_integers:
            if i > num:
                num = i
        return num
    return None
