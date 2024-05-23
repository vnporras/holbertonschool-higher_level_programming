#!/usr/bin/python3
"""Defines a class Rectangle
"""
class Rectangle:
    """Represents a rectangle
    """
    def __init__(self, width=0, height=0):
            """Initializes a rectangle"""
            self.__height = height
            self.__width = width

    @property
    def height(self):
        """getter for the instance attribute height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter for the instance attribute height"""
        if not type(value) is int:
            """raise a TypeError exception with the message height must be an integer"""
            raise TypeError("height must be an integer")
        
        if self.__height < 0:
            """raise a ValueError exception with the message height must be >= 0"""
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
            """raise a TypeError exception with the message width must be an integer"""
            raise TypeError("width must be an integer")
        
        if self.__width < 0:
            """raise a ValueError exception with the message width must be >= 0"""
            raise ValueError("width must be >= 0")
        
        self.__width = value
