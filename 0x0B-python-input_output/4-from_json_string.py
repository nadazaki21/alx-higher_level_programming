#!/usr/bin/python3
""" module 4 """
from json import dumps

def from_json_string(my_str):
    """  function that returns an object
    (Python data structure) represented by a JSON string """
    return (dumps(my_str))
