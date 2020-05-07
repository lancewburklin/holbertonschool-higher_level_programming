#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set_1 | set_2
    exclude = set_1 & set_2
    new_set = new_set - exclude
    return (new_set)
