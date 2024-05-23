#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represents a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle"""
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

    @property
    def height(self):
        """getter for the instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the instance attribute height"""
        if not type(value) is int:
            raise TypeError("height must be an integer")

        if self.__height < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    @property
    def width(self):
        """getter for the instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the instance attribute width"""
        if not type(value) is int:

            raise TypeError("width must be an integer")

        if self.__width < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    def area(self):
        """Calculates the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * self.__width) + (2 * self.__height)

    def __str__(self):
        """Returns the string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""

        print_rectangle = ""
        for _ in range(self.height):
            print_rectangle += "#" * self.width + "\n"
        return print_rectangle.strip()

    def __repr__(self):
        """Returns the string representation of the rectangle"""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
