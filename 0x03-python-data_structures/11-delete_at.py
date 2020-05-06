#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx > len(my_list) - 1:
        return (my_list)
    if idx < 0:
        return (my_list)
    newe_list = []
    for i in range(len(my_list) - 1):
        if i == idx:
            my_list.remove(my_list[i])
    return (my_list)
