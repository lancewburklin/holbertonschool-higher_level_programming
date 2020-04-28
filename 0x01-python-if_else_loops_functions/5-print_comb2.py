#!/usr/bin/python3
x = False
for i in range(0, 100):
    if i == 99:
        x = True
    if i < 10:
        print("{:d}".format(0), end="")
    if i != 100:
        print("{:d}{:s}{:s}".format(i, "" if x else ",", "\n" if x else " "), end="")
