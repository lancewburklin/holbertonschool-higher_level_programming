#!/usr/bin/python3

"""Prints a square"""


def print_square(size):
    """Square function"""
    if type(size) == float and size < 0:
        raise TypeError('size must be an integer')
    if type(size) not in [int]:
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    i = 0
    while i < size:
        print("#" * size)
        i += 1
