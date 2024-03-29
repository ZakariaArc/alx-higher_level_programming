#!/usr/bin/python3
"""
module containing a function that checks
if an object is an instance of a class inherited from a specified class
"""


def inherits_from(obj, a_class):
    """checks if obj is an instance of a class inherited from a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
