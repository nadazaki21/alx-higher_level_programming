#!/usr/bin/python3
""" module 2 """


def append_write(filename="", text=""):
    """ function that writes a string to a text file
    (UTF8) and returns the number of characters written """
    with open(filename, "a", encoding="UTF-8") as file:
        start = file.tell()
        file.write(text)
        finish = file.tell()
    return finish - start
