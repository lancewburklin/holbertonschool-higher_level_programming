#!/usr/bin/python3
"""
TIme for a post request yo
"""

if __name__ == "__main__":
    import urllib.parse
    import urllib.request
    import sys
    url = sys.argv[1]
    email = {"email": sys.argv[2]}
    info = urllib.parse.urlencode(email)
    info = info.encode('ascii')
    req = urllib.request.Request(url, info)
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print(the_page.decode('utf8'))
