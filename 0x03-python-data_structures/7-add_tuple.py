#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = [0, 0]
    if tuple_a == ():
        new_tuple = [0, 0]
    elif len(tuple_a) == 1:
        new_tuple[0] = tuple_a[0]
    else:
        new_tuple[0] = tuple_a[0]
        new_tuple[1] = tuple_a[1]

    if tuple_b == ():
        new_new_tuple = (new_tuple[0], new_tuple[1])
        return (new_new_tuple)
    if len(tuple_b) == 1:
        new_tuple[0] = new_tuple[0] + tuple_b[0]
    else:
        new_tuple[0] = new_tuple[0] + tuple_b[0]
        new_tuple[1] = new_tuple[1] + tuple_b[1]
    new_new_tuple = (new_tuple[0], new_tuple[1])
    return (new_new_tuple)
