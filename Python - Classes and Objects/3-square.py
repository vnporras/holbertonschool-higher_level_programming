#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        self.__size = size

        if not type(self.__size) is int:
            raise TypeError("size must be an integer")
        
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        
    def area(self):
        return self.__size * self.__size


my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
