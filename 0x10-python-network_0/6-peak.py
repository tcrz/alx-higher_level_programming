#!/usr/bin/python3
"""find peak in a  list of unsorted integers"""


def find_peak(list_of_integers):
    """function to find peak"""

    if len(list_of_integers) == 0:
        return None
    else:
        return max(list_of_integers)
