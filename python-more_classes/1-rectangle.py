#!/usr/bin/python3
"""Defines a class Rectangle
"""


class Rectangle:
    """Represents a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes a rectangle"""
        self.width = width
        self.height = height

    @property
    def height(self):
        """getter for the instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """getter for the instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
