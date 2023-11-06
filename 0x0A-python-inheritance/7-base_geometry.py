#!/usr/bin/python3
"""
module for BaseGeometry class
"""


class BaseGeometry:
    """a BaseGeometry class"""
    def area(self):
        """method to compute this area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """method for validating the value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
