#!/usr/bin/python3
"""
module containing a function add_attribute
"""


def add_attribute(obj, attr, value):
    """add a new attribute to an object if it's possible"""
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")
