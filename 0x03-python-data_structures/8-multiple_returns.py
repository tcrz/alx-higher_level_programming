#!/usr/bin/python3

def multiple_returns(sentence):

    length = len(sentence)
    if length != 0:
        tuple = length, sentence[0]
    else:
        tuple = length, "None"

    return tuple

sentence = "dsdssd"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))
