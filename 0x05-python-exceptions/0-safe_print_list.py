#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    ending = ""
    while i < x:
        try:
            if i == x-1:
                ending = '\n'
            print("{}".format(my_list[i]), end=ending)
            i = i + 1
        except:
            print("")
            return(i)
    return(i)
