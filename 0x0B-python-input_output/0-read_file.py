#!/usr/bin/python3
""" module 0 """


def read_file(filename=""):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read
        print(data)
