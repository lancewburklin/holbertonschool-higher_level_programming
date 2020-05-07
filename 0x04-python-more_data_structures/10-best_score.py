#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return (None)
    if not a_dictionary.values():
        return (None)
    allvalue = list(a_dictionary.values())
    top = allvalue[0]
    for i in (allvalue):
        if i > top:
            top = i
    for n in (a_dictionary.keys()):
        if a_dictionary.get(n) == top:
            topname = n
    return topname
