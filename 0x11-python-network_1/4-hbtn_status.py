#!/usr/bin/python3
"""
Using the requests package
"""


if __name__ == "__main__":
    import requests
    x = requests.get('https://intranet.hbtn.io/status')
    x = x.text
    print("\t- type: {}".format(type(x)))
    print("\t- content: {}".format(x))
