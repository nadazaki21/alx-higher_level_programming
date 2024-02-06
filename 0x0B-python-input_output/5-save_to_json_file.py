#!/usr/bin/python3
""" module 5 """
from json import dumps


def save_to_json_file(my_obj, filename):
    """  function that returns the JSON
    representation of an object (string) """
    json_obj = dumps(my_obj)
    with open(filename, "w") as file:
        file.write(json_obj)
