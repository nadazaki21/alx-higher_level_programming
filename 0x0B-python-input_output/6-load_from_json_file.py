#!/usr/bin/python3
""" module 5 """
from json import loads


def load_from_json_file(filename):
    """  function that creates an Object from a “JSON file """
    with open(filename, 'r') as file:
        return (loads(file))
