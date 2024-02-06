#!/usr/bin/python3
""" module 1 """


def write_file(filename="", text=""):
    """ function that writes a string to a text file
    (UTF8) and returns the number of characters written """
    with open(filename, "w", encoding="UTF-8") as file:
        start = file.tell()
        file.write(text)
        finish = file.tell()
    return finish - start
