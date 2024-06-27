#!/usr/bin/python3

"""class"""
class MyList(list):
    """class that inherits from class list"""
    def print_sorted(self):
        """print the ascending list"""
        self.sort()
        print(self)
