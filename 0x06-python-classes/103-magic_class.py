#!/usr/bin/python3

"""It defines a MagicClass matching a bytecode provided."""

import math


class MagicClass:
    """
    Represents a class with methods for circle calculations.

    Attributes:
        __radius (float): The radius of the circle.

    Methods:
        __init__(self, radius=0): Initializes a MagicClass instance
                                  with a radius.
        area(self): Calculates the area of the circle.
        circumference(self): Calculates the circumference of the circle.
    """

    def __init__(self, radius=0):
        """
        Initializes a MagicClass instance with a given radius.

        Args:
            radius (float): The radius of the circle.

        Raises:
            TypeError: If the radius is not a number (float or integer).
        """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = float(radius)

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float: The circumference of the circle.
        """
        return 2 * math.pi * self.__radius
