#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        new_list = my_list.copy()
        if idx > (len(my_list) - 1):
            return (new_list)
        elif idx < 0:
            return (new_list)
        for i in range(len(my_list)):
            if i == idx:
                new_list[i] = element
                return (new_list)
