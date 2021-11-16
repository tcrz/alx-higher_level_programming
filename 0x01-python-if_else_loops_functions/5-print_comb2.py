#!/usr/bin/python3
for i in range(0, 10):
    for x in range(0, 10):
        if i == 9 and x == 9:
            print("{0}{1}".format(i, x), end="\n")
        else:
            print("{0}{1}".format(i, x), end=", ")
