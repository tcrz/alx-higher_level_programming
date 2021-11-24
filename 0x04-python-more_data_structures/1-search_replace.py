#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]

    idx = new_list.index(search)
    new_list.pop(idx)
    new_list.insert(idx, replace)
    return new_list
