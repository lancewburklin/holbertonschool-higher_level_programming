#!/usr/bin/python3
for i in range(0, 9):
    for x in range(i, 10):
        if x > i and x * i != 72:
            print("{:d}{:d}".format(i, x), end=", ")
        elif x * i == 72:
            print("{:d}{:d}".format(i, x), end="\n")
