#!/usr/bin/python3
"""Empty class Square that defines a square."""


class Square:
    """Empty class Square that defines a square."""

    def __init__(self, size=0):
        """Initializes the data."""
        self.__size = size

        if not type(self.__size) is int:
            """Raise an error if size is not an integer."""
            raise TypeError("size must be an integer")

        if self.__size < 0:
            """Raise an error if size is less than 0."""
            raise ValueError("size must be >= 0")
