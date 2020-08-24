#!/usr/bin/python3
"""
Using the Github API
"""


if __name__ == "__main__":
    import sys
    import requests
    sess = requests.Session()
    sess.auth = (sys.argv[1], sys.argv[2])
    thing = sess.get('https://api.github.com/user').json()
    print(thing.get("id"))
