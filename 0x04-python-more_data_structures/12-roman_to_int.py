#!/usr/bin/python3
def roman_to_int(roman_string):
    rstr = roman_string
    total = 0
    if rstr:
        r = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    for i in range(len(rstr)):
        if i > 0 and rstr[r[i]] > rstr[r[i - 1]]:
            total += rstr[r[i]] - (2 * rstr[r[i - 1]])
        else:
            total += rstr[r[i]]
