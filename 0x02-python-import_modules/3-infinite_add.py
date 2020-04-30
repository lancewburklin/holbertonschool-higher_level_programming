#!/usr/bin/python3
def main():
    import sys
    args = sys.argv
    num = 0
    for i in args[1:]:
        num = num + int(i)
    print("{}".format(num))

if __name__ == "__main__":
    main()
