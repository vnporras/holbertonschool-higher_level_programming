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

    def area(self):
        """Calculates the area of a rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Returns a string representation of a rectangle"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initializes a square"""
        self.__size = size
        self.integer_validator(size, self.__size)
        super().__init__(self.__size, self.__size)

    def area(self):
        """Calculates the area of a square"""
        return self.__size * self.__size
    
    def __str__(self):
        """Returns a string representation of a square"""
        return "[Square] {}/{}".format(self.__size, self.__size)