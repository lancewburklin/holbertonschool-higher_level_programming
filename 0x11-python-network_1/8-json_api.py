#!/usr/bin/python3
"""
Send a letter
"""


if __name__ == "__main__":
    import sys
    import requests
    if len(sys.argv) != 1:
        test = str(sys.argv[1])
    else:
        test = ""
    thing = requests.post('http://0.0.0.0:5000/search_user', data={'q': test})
    try:
        if len(thing.json()) == 0:
            print("No result")
        else:
            derulo = thing.json()
            print("[{}] {}".format(derulo.get("id"), derulo.get("name")))
    except:
        print("Not a valid JSON")
