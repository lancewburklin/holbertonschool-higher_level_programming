#!/usr/bin/python3
"""
Time to get some headers
"""


if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(response.info().get('X-Request-Id'))
