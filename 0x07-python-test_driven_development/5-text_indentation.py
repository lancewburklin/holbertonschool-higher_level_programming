#!/usr/bin/python3

"""Indents text with special characters"""


def text_indentation(text):
    """Prints text"""
    if type(text) != str:
        raise TypeError('text must be a string')
    i = 0
    while i < len(text):
        if i == 0 and text[i] == ' ':
            while i < len(text) and text[i] == " ":
                i += 1
            if i == len(text):
                break
        print("{}".format(text[i]), end="")
        i += 1
        if text[i - 1] in ['.', '?', ':']:
            print("\n")
            if i != len(text) - 1:
                while i < len(text) and text[i] == " ":
                    if text[i] == " ":
                        i += 1
