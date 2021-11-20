#!/usr/bin/python3

def multiple_returns(sentence):

    length = len(sentence)
    if length != 0:
        str = sentence
        tuple = length, str[0]
    else:
        str = None
        tuple = length, str
    return tuple
