#!/usr/bin/python3
from sys import argv

sum = 0
if __name__ == "__main__":
    if len(argv) > 1:
        for i in range(1, len((argv))):
            sum = sum + int(argv[i])
    print(sum)
