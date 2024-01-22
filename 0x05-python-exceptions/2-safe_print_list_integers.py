#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        integer_count = 0
        for i in my_list[:x]:
            print("{:d}".format(i))
            integer_count = integer_count + 1
    except (IndexError, TypeError, ValueError):
        print("list index out of range")
    finally:
        return (integer_count)
