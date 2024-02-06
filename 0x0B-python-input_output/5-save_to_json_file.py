#!/usr/bin/python3
""" module 5 """
from json import dumps


def save_to_json_file(my_obj, filename):
    """  function that returns the JSON
    representation of an object (string) """
    with open(filename, "w") as file:
        file.write(dumps(my_obj))
