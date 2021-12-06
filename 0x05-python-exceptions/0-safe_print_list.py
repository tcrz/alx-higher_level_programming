#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    for each in my_list:
        len += 1
    try:
        for i in range(x):
            print(my_list[i], end="")
        print("")
        return x
    except IndexError:
        print("")
        return len
