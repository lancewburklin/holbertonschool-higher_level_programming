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

with open('add_item.json', mode='a', encoding='utf-8') as a_file:
    try:
        old_args = load_from_file('add_item.json')
        if old_args != []:
            args = old_args + args
        save_to_file(args, 'add_item.json')
        a_file.write('\n')
    except:
        save_to_file(args, 'add_item.json')
        a_file.write('\n')
