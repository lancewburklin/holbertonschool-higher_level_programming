#!/usr/bin/python3
"""
Returns Python representation of JSON
"""


def from_json_string(my_str):
    """Translates JSON to Python"""
    import json
    return json.loads(my_str)
