#!/usr/bin/python3

class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
        
    def area(self):
        return self.__size * self.__size
    
    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, value):
        self.__size = value

        if not type(self.__size) is int:
            raise TypeError("size must be an integer")
        
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        self.__position = value

        if not type(self.__position) is tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        
    def my_print(self):
        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                print("")
                
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    if j == 0:
                        print("_" * self.__position[0], end="")
                    print("#", end="")
                print()
            


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")