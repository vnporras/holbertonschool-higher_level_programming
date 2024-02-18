#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for index, value in enumerate(my_list):
            if (index < x):
                print(str(value), end="")
                counter += 1
        print()
        return counter
    except Exception:
        return counter
