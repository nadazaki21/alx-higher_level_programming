#!/usr/bin/python3


def add_attribute(self, name, value):
    if type(self) is str or type(self) is tuple or type(self) is frozenset:
        raise TypeError("can't add new attribute")
    self.__dict__[name] = value
