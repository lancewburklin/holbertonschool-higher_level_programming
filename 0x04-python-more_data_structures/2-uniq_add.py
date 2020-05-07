#!/usr/bin/python3
def uniq_add(my_list=[]):
    summ = 0
    new_list = list.copy(my_list)
    new_list = list(set(new_list))
    for i in range(len(new_list)):
        summ = summ + new_list[i]
    return (summ)
