#!/usr/bin/python3
for i in range(97, 123):
    if i != ord('e') and i != ord('q'):
        print("{:c}".format(i), end="")
