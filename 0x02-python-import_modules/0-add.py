#!/usr/bin/python3
def main():
    import add_0 as func
    a = 1
    b = 2
    result = func.add(a, b)
    print("{} + {} = {}".format(a, b, result))
if __name__ == "__main__":
    main()
