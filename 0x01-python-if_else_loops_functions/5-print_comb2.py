#!/usr/bin/python3
for x in range(0, 100):
    if x == 99:
        print(x)
    else:
        print("{:0>2}".format(x), end=", ")
