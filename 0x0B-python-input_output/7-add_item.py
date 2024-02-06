#!/usr/bin/python3
""" module 7 """
from sys import argv
from json import dumps
import os


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
old_list = []

if (os.path.exists("add_item.json") and os.path.getsize("add_item.json") != 0):
    old_list = list(load_from_json_file("add_item.json"))

    q = argv[1:]
    old_list.extend(q)
    save_to_json_file(old_list, "add_item.json")
else:
    q = argv[1:]
    old_list.extend(q)
    save_to_json_file(old_list, "add_item.json")
