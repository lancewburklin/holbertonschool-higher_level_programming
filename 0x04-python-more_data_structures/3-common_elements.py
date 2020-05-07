#!/usr/bin/python3
def common_elements(set_1, set_2):
    terms = []
    set_1 = list(set_1)
    set_2 = list(set_2)
    for i in range(len(set_1)):
        for n in range(len(set_2)):
            if set_1[i] == set_2[n]:
                terms.append(set_1[i])
    return (terms)
