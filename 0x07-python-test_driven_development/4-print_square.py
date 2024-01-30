#!/usr/bin/python3
"""
function that prints a square with the character #.
"""


def print_square(size):
    """ prints a sqaure with the # by specifing its side lenght which is size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif size == 0:
        print()
    else:
        for i in range(size):
            for j in range(size):
                print("#", end="")
            print("\n", end="")
