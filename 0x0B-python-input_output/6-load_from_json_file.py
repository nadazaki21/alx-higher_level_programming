#!/usr/bin/python3
""" module 5 """
from json import load


def load_from_json_file(filename):
    """  function that creates an Object from a “JSON file """
    with open(filename) as file:
        return (load(file))
