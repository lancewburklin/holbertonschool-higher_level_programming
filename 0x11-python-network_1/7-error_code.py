#!/usr/bin/python3
"""
Handling error codes
"""


if __name__ == "__main__":
    import requests
    import sys
    info = requests.get(sys.argv[1])
    if info.status_code > 400:
        print("Error code: {}".format(info.status_code))
    else:
        print(info.text)
