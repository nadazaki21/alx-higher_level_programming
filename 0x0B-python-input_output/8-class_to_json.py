#!/usr/bin/python3
""" module 8 """
import json


def class_to_json(obj):
    """  function that returns the dictionary description
    with simple data structure (list, dictionary, string,
    integer and boolean) for JSON serialization of an object """
    result = {}
    for attr_name, attr_value in obj.__dict__.items():
        if isinstance(attr_value, (list, dict, str, int, bool)):
            result[attr_name] = attr_value
    #return vars(obj)
    return result
