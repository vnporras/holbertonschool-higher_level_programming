#!/usr/bin/python3
"""Defines a class Rectangle"""
class Rectangle:
    """Represents a rectangle"""
    
    def __init__(self, width=0, height=0):
        """Initializes a rectangle"""
        self.__height = height
        self.__width = width

    @property
    def height(self):
        """getter for the height attribute"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter for the height attribute"""
        if not type(value) is int:
            """Raise an exception if the value is not an integer"""
            raise TypeError("height must be an integer")
        
        if self.__height < 0:
            """Raise an exception if the value is less than 0"""
            raise ValueError("height must be >= 0")
        
        self.__height = value

    @property
    def width(self):
        """getter for the width attribute"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter for the width attribute"""
        if not type(value) is int:
            """Raise an exception if the value is not an integer"""
            raise TypeError("width must be an integer")
        
        if self.__width < 0:
            """Raise an exception if the value is less than 0"""
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
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print("#", end="")
            
            if i == self.__height - 1:
                pass
            else:
                print()
        
        return ""
    
    def __repr__(self):
        """Returns the string representation of the rectangle"""
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
    
    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        print("Bye rectangle...")
