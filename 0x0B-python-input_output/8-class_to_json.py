#!/usr/bin/python3
"""
Defines a Python class-to-JSON function.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.

    Args:
        obj: An instance of a Class with serializable attributes.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
