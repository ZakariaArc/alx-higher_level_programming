#!/usr/bin/python3
"""
module containing a function that checks
if an object is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """checks if obj is exactly an instance of a_class."""
    return type(obj) is a_class
