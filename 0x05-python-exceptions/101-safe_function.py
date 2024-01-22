#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        result = fct()
    except Exception as e:
        print("{}".format(e))
        result = None
    return result
