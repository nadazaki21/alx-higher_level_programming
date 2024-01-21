#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        print("0 arguments.")
    elif (len(argv) == 1):
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(len(argv)))
        for i in range(len(argv)):
            print("{}: {}".format(i, argv[i]))
