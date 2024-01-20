#!/usr/bin/python3
for i in range(9):
    for j in range(((i*11)+1), ((i*10)+10)):
        if (j != 89):
            print("{:02d}".format(j), end=", ")
        else:
            print("{:02d}\n".format(j), end="")
