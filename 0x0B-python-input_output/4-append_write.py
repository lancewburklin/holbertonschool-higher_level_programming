#!/usr/bin/python3
"""
Appends text to a file
"""


def append_write(filename="", text=""):
    """Here is where we append"""
    with open(filename, mode='a', encoding='utf-8') as a_file:
        a_file.write(text)
    return len(text)
