#!/usr/bin/python3
"""Module 7-add_item.py"""

import sys

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file


try:
    items = load_json("add_item.json")
except (ValueError, FileNotFoundError):
    items=[]
items.extend(sys.argv[1:])
save_to_json_file(items, "add_item.json")
