#!/usr/bin/env python3
flag = 1
for i in range(122, 96, -1):
    print("{}".format(chr(i)) if flag else "{}".format(chr(i-32)) ,end="")
    flag = not flag