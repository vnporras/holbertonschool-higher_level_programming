#!/usr/bin/python3
"""Empty class MyList that inherits from list."""
class MyList(list):
    """Empty class MyList that inherits from list and use the method print_sorted."""    
    def print_sorted(self):
        """Print the sorted list."""
        print(sorted(self))
