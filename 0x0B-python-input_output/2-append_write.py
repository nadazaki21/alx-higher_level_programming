#!/usr/bin/python3
""" module 0 """


def read_file(filename=""):
    """ function that reads a text file (UTF8) and prints it to stdout """
    with open(filename, 'r') as file:
        data = file.read
        print(data)
