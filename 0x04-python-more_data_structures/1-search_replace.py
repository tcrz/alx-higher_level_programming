#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for i in my_list:
        if i != search:
            new_list.append(i)
        else:
            i = replace
            new_list.append(i)
    return new_list
