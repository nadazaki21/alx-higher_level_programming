#!/usr/bin/python3
""" function that checks is an object is a specific type """


def is_same_class(obj, a_class):
    """ checks if the igven object is the type given """
    if type(obj) is a_class:
        return True
    else:
        return False
