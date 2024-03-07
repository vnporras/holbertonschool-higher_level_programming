#!/usr/bin/python3
"""Rectangle class that inherits from Base"""
from base import Base

class Rectangle(Base):
    """Rectangle class that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor of the class Rectangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """getter of the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of the width attribute"""
        self.__width = value

    @property
    def height(self):
        """getter of the height attribute"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter of the height attribute"""
        self.__height = value

    @property
    def x(self):
        """getter of the x attribute"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """setter of the x attribute"""
        self.__x = value

    @property
    def y(self):
        """getter of the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter of the y attribute"""
        self.__y = value
