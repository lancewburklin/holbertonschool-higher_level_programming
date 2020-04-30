#!/usr/bin/python3
import sys
args = sys.argv
num = 0
for i in args[1:]:
    num = num + int(i)
print("{}".format(num))
