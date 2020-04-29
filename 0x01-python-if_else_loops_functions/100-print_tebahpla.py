#!/usr/bin/python3
for i, x in zip(range(122, 96, -1), range(1, 27)):
    print("{:c}".format(i - 32 if x % 2 == 0 else i), end="")
