#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        case = ord(str[i])
        if case > 96 and case < 123:
            case = case - 32
        print("{:c}".format(case), end="")
    print("")
