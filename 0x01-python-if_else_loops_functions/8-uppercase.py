#!/usr/bin/python3
def uppercase(str):
    a = 96
    b = 123
    for i in str:
        print("{}".format(chr(ord(i) - 32) if a < ord(i) < b else i), end="")
    print("{}".format("\n"), end="")
