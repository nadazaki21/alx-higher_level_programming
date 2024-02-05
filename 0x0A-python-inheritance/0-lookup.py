#!/usr/bin/python3
"""
function that returns the list of available attributes and methods of an object
"""


def lookup(obj):
    """ lists the attributes in a class """
    return list(dir(obj))
