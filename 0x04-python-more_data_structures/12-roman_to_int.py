#!/usr/bin/python3
def roman_to_int(roman_string):
    rstr = roman_string
    total = 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if rstr and type(rstr) == str:
        for i in range(len(rstr)):
            if i > 0 and roman[rstr[i]] > roman[rstr[i - 1]]:
                total += roman[rstr[i]] - (2 * roman[rstr[i - 1]])
            else:
                total += roman[rstr[i]]
        return total
    return 0
