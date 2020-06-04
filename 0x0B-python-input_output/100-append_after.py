#!/usr/bin/python3
"""
Appends to a spot in a file
"""


def append_after(filename="", search_string="", new_string=""):
    """Finds search_string in filename and appends new_string"""
    line_number = 0
    with open(filename, mode='r', encoding='utf-8') as a_file:
        lines = a_file.readlines()

    for line in lines:
        line_number += 1
        if search_string in line:
            lines.insert(line_number, new_string)

    with open(filename, mode='w', encoding='utf-8') as a_file:
        lines = "".join(lines)
        a_file.write(lines)
