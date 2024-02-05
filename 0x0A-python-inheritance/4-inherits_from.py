#!/usr/bin/python3
"""
===================================
module with method inherits_from
===================================
"""


def inherits_from(obj, a_class):
    """Method that return True if an object is an instance of a class
    that inherited from"""

    if issubclass(obj, a_class):
        if type(obj) is a_class:
            return False
        return True
    else:
        return False
