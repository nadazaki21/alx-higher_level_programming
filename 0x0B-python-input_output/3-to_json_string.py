#!/usr/bin/python3
""" module 3 """
from json import dumps


def to_json_string(my_obj):
    """  function that returns the JSON
    representation of an object (string) """
    json_string = dumps(my_obj)
    return (json_string)
