#!/usr/bin/python3
"""
Gets the JSON respresentation of a string
"""


def to_json_string(my_obj):
    """Converting to JSON"""
    import json
    test = json.dumps(my_obj)
    return test
