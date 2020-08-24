#!/usr/bin/python3
"""
Get Request headers
"""


if __name__ == "__main__":
    import requests
    import sys
    stuff = requests.get(sys.argv[1])
    print(stuff.headers['X-Request-Id'])
