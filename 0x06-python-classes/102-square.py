#!/usr/bin/python3

"""It defines a class square."""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializes a square

        Args:
            size (int): The size of the square. Default is 0.

        Raises:
            TypeError: If `size` is not a number (float or integer).
            ValueError: If `size` is less than 0.

        """
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square.

        Returns:
            float or int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (float or int): The new size of the square.

        Raises:
            TypeError: If `value` is not a number (float or integer).
            ValueError: If `value` is less than 0.

        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number (float or integer)")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            float or int: The area of the square.

        """
        return self.__size ** 2

    def __eq__(self, other):
        """Compares two squares for equality based on their areas.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if the areas are equal, False otherwise.

        """
        return self.area() == other.area()

    def __ne__(self, other):
        """Compares two squares for inequality based on their areas.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if the areas are not equal, False otherwise.

        """
        return self.area() != other.area()

    def __lt__(self, other):
        """Compares two squares based on their areas.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if self.area() < other.area(), False otherwise.

        """
        return self.area() < other.area()

    def __le__(self, other):
        """Compares two squares based on their areas.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if self.area() <= other.area(), False otherwise.

        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compares two squares based on their areas.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if self.area() > other.area(), False otherwise.

        """
        return self.area() > other.area()

    def __ge__(self, other):
        """Compares two squares based on their areas.

        Args:
            other (Square): The square to compare.

        Returns:
            bool: True if self.area() >= other.area(), False otherwise.

        """
        return self.area() >= other.area()
