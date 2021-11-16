#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ''
    i = 0
    for c in str:
        if i != n:
            newstr += str[i]
        i += 1
    return newstr
