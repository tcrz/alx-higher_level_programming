#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    for character in my_string:
        if character not in 'Cc':
            newstring += character
    return newstring
