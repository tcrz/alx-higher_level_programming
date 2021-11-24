#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if i != search:
            new_list.append(i)
        else:
            i = replace
            new_list.append(i)
    # idx = new_list.index(search)
    # new_list.pop(idx)
    # new_list.insert(idx, replace)
    return new_list
