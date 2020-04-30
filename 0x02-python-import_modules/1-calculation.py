#!/usr/bin/python3
import calculator_1 as func
a = 10
b = 5
adda = func.add(a, b)
suba = func.sub(a, b)
mula = func.mul(a, b)
diva = func.div(a, b)
matharray = [adda, suba, mula, diva]
oparray = ["+", "-", "*", "/"]

for i, x in zip(matharray, oparray):
    print("{} {} {} = {}".format(a, x, b, i))
