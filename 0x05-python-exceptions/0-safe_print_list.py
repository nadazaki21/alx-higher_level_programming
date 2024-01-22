#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list[:x]:
            print("{}".format(i), end="")
            count = count + 1
        print()
    except IndexError:
        print("index of list out of boundaries")
    finally:
        return count
