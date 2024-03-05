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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area"""
        if not type(rect_1) is Rectangle:
            """raise a TypeError exception with the message rect_1 must be an instance of Rectangle"""
            raise TypeError("rect_1 must be an instance of Rectangle")
        
        if not type(rect_2) is Rectangle:
            """raise a TypeError exception with the message rect_2 must be an instance of Rectangle"""
            raise TypeError("rect_2 must be an instance of Rectangle")
        
        rect1_area = rect_1.area()
        react2_area = rect_2.area()

        if rect1_area >= react2_area:
            return rect_1
        else:
            return rect_2
        
    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance with width == height == size"""
        return cls(size, size)

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
            raise TypeError("width must be an integer")
        
        if self.__width < 0:
            """raise a ValueError exception with the message width must be >= 0"""
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
                print(self.print_symbol, end="")
            
            if i == self.__height - 1:
                pass
            else:
                print()
        
        return ""
    
    def __repr__(self):
        """Returns the formal string representation of the rectangle"""
        return "Rectangle(" + str(self.__width) + ", " + str(self.__height) + ")"
    
    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
