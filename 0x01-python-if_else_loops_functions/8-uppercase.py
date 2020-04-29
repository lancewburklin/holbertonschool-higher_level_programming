#!/usr/bin/python3
def uppercase(str):
    for i in str:
        print("{}".format(chr(ord(i) - 32) if 96 < ord(i) < 123 else i), end="")
    print("{}".format("\n"), end="")
