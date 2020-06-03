#!/usr/bin/python3
"""
Rads n lines of a file
"""


def read_lines(filename="", nb_lines=0):
    num_lines = 0
    with open(filename, encoding='utf-8') as a_file:
        if nb_lines <= 0:
            print(a_file.read())
        else:
            for lines in a_file:
                if num_lines < nb_lines:
                    print("{}".format(lines.rstrip()))
                    num_lines += 1
