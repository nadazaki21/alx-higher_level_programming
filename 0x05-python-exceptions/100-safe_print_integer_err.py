#!/usr/bin/python3
from sys import stderr
def safe_print_integer_err(value):
    result = None
    try:
        print("{:d}".format(value))
        result = True
    except (TypeError, ValueError) as e:
        stderr.write("Exception: {}\n".format(e))
        result = False
    finally:
        return result
