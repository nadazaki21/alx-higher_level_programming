#!/usr/bin/python3
""" module 0 """


def read_file(filename=""):
    """ function that print content of file """
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
