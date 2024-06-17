#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Represents a rectangle
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a rectangle"""
        self.height = height
        self.width = width
        type(self).number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not type(rect_1) is Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not type(rect_2) is Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        rect1_area = rect_1.area()
        react2_area = rect_2.area()

        if rect1_area >= react2_area:
            return rect_1
        else:
            return rect_2

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
