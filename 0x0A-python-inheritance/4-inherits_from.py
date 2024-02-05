#!/usr/bin/python3
"""
function that returns True if the object is an instance
of a class that inherited (directly or indirectly)
from the specified class ; otherwise False.
"""


def inherits_from(obj, a_class):
    """ check if object belons to inheritrance chain """
    obj_class = type(obj)
    if issubclass(obj_class, a_class):
        if obj_class is a_class:
            return False
        return True
    else:
        return False
