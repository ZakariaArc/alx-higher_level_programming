#!/usr/bin/python3
"""
Module containing a class BaseGeometry with
area() and integer_validator() methods.
"""

class BaseGeometry:
    def area(self):
        """Raises an Exception with the message 'area() is not implemented'"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates value as an integer."""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))

