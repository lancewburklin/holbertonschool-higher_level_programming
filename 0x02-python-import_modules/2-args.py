#!/usr/bin/python3
def main():
    import sys
    args = sys.argv
    arglen = len(args) - 1
    count = 0
    if arglen == 0:
        print("0 arguments.")
    elif arglen == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arglen))
    for i in args[1:]:
        count = count + 1
        print("{}: {}".format(count, i))

if __name__ == "__main__":
    main()
