#!/usr/bin/python3
def main():
    import calculator_1 as func
    import sys

    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = args[2]
    ops = ["+", "-", "*", "/"]
    for i in ops:
        if i == operator:
            break
        if i == "/":
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    a = int(args[1])
    b = int(args[3])
    if operator == "+":
        result = func.add(a, b)
    elif operator == "-":
        result = func.sub(a, b)
    elif operator == "*":
        result = func.mul(a, b)
    elif operator == "/":
        result = func.div(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))

if __name__ == "__main__":
    main()
