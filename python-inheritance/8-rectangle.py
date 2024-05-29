#!/usr/bin/python3

"""Defines a class BaseGeometry"""
class BaseGeometry:
    """Represents a base geometry"""

    def area(self):
        """Not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value"""
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """Represents a rectangle"""

    def __init__(self, width, height):
        """Initializes a rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator(width, self.__width)
        self.integer_validator(height, self.__height)
