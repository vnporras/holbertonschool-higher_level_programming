#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        self.__size = size

        if not type(self.__size) is int:
            raise TypeError("size must be an integer")
        
        if self.__size < 0:
            raise ValueError("size must be >= 0")
