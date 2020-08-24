#!/usr/bin/python3
"""
Get the status from hbtn.io
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print("\t- type: {}".format(type(the_page)))
        print("\t- content: {}".format(the_page))
        print("\t- utf8 content: {}".format(the_page.decode('utf8')))
