#!/usr/bin/python3
def remove_char_at(str, n):
    newstr = ""
    for i, x in zip(str, range(0, len(str) + 1)):
        if x != n:
            newstr = newstr + i
    return (newstr)
