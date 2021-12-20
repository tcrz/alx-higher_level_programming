#!/usr/bin/python3
"""
1-my_list module
"""


class MyList(list):
    """Class that inherits from list"""
    def print_sorted(self):
        """prints the list sorted in ascending order"""
        newlist = self[:]
        newlist.sort()
        print(newlist)
