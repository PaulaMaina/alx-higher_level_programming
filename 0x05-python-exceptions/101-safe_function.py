#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)
    except (ZeroDivisionError, TypeError, IndexError, ValueError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return None
