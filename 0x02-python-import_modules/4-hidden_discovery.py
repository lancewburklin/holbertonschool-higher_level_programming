#!/usr/bin/python3
def main():
    import hidden_4
    names = dir(hidden_4)
    for i in names:
        if i[0] != "_":
            print("{}".format(i))

if __name__ == "__main__":
    main()
