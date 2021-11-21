#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        str = None
        tuple = length, str
    else:
        str = sentence
        tuple = length, str[0]
    return tuple
