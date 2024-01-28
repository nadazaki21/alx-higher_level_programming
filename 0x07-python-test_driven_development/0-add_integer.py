#!/usr/bin/python3
"""
task 0
adding 2 inetegers
numbers in strings are not converted to inetgers
floats are converted to inetegers
"""


def add_integer(a, b=98):
    """ adds 2 integers """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    sum = int(a) + int(b)

    return sum
