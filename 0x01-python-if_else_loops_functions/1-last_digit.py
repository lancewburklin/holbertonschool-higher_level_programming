#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
stat = "nothing"
iszero = "nothing"

if number < 0:
    newnum = -number
    last = -(newnum % 10)

if last > 5:
    stat = "and is greater than 5"
elif last < 6:
    stat = "and is less than 6"
else:
    stat = "is 0"

if last is 0:
    iszero = "and is 0"
else:
    iszero = "and not 0"

print("Last digit of {:d} is {:d} {} {}".format(number, last, stat, iszero))
