#!/usr/bin/python3
"""
Using Requests with a POST request
"""


if __name__ == "__main__":
    import requests
    import sys
    info = requests.post(sys.argv[1], data = {'email': sys.argv[2]})
    print(info.text)
