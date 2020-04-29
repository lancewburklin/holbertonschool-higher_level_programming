#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    nummy = number % 10
    print("{}".format(nummy), end="")
    return(nummy)
