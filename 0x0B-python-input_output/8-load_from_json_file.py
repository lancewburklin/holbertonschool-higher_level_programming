#!/usr/bin/python3
"""
Loads some JSON from a file
"""


def load_from_json_file(filename):
    """JSON file"""
    import json
    with open(filename, 'r', encoding='utf-8') as a_file:
        return json.load(a_file)
