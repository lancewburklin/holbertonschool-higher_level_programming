#!/usr/bin/python3
"""
TIme for another request
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    req = urllib.request.Request(sys.argv[1])
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as thingy:
        print("Error code: {}".format(thingy.code))
    else:
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode('utf8'))
