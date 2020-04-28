#!/usr/bin/python3
for i in range(0, 100):
    if i < 10:
        print("{:d}".format(0), end="")
    if i != 100:
        print("{:d}{:s}".format(i, ", " if i != 99 else "\n"), end ="")
