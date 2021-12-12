#!/usr/bin/python3
"""
This is the 5-text_indentation module
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: . , ?

    Args:
        text (str): a piece of text
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("{}\n".format(text[i]))
        else:
            if text[i] != " ":
                print(text[i], end="")
            elif text[i] == " " and text[i-1] == '.' or text[i-1] == '?':
                pass
            elif text[i] == " " and text[i-1] == ':':
                pass
            else:
                print(text[i], end="")
