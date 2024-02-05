#!/usr/bin/python3
""" this module has a function that add
new attribbutes to valid kinds of objects """


def add_attribute(self, name, value):
    """ adding attributed to valid objects """
    if isinstance(self, (str, tuple, frozenset)):
        raise TypeError("can't add new attribute")
    self.__dict__[name] = value
