#!/usr/bin/python3
"""
Opening a file
"""


def read_file(filename=""):
    """Reading a file"""
    with open(filename, encoding='utf-8') as file_desc:
        print(file_desc.read())
