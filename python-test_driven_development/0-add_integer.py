#!/usr/bin/python3
"""
This module supplies one function, add_integer.
It adds two integers or floats (cast to int) together.
No external modules are used.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats cast to integers.
    Returns an integer: the addition of a and b.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
