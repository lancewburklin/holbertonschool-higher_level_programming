#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_string = list(my_string)
        for i in range(len(my_string)):
            if ord(my_string[i]) == 99 or ord(my_string[i]) == 67:
                new_string.remove(my_string[i])
        my_string = "".join(new_string)
    return (my_string)
