#!/usr/bin/python3
""" module 5 """
from json import dump


def save_to_json_file(my_obj, filename):
    """  function that returns the JSON
    representation of an object (string) """
    with open(filename, "w", encoding="utf-8") as file:
        dump(my_obj, file)
