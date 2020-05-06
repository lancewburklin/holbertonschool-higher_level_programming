#!/usr/bin/python3
def multiple_returns(sentence):
    eltuple = [0, None]
    if sentence != "":
        eltuple[0] = len(sentence)
        eltuple[1] = sentence[0]
    thetuple = (eltuple[0], eltuple[1])
    return (thetuple)
