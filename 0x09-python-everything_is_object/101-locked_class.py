#!/usr/bin/python3
"""
This module defines a class LockedClass that
restricts the creation of instance attributes.
The only allowed instance attribute is 'first_name'.
"""


class LockedClass:
    """
    This class restricts the creation of new instance attributes,
    except for 'first_name'.
    """

    __slots__ = ['first_name']
