#!/usr/bin/python3
""" module 3 """
from json import dump


def to_json_string(my_obj):
    """  function that returns the JSON representation of an object (string) """
    return (dump(my_obj))