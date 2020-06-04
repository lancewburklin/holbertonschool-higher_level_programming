#!/usr/bin/python3
"""
Adds arguments to a list
"""


import json
import sys
save_to_file = __import__('7-save_to_json_file').save_to_json_file
load_from_file = __import__('8-load_from_json_file').load_from_json_file

args = sys.argv
args = list(args)
del args[0]

try:
    a_fie = load_from_file('add_item.json')
except:
    a_file = []
items = a_file + args
save_to_file(items, 'add_item.json')
