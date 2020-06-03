#!/usr/bin/python3
"""
Finds the number of lines in a file
"""


def number_of_lines(filename=""):
    """Start of function"""
    line_number = 0
    with open(filename, encoding='utf-8') as file_desc:
        for lines in file_desc:
            line_number += 1
    return line_number
