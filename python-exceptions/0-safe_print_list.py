#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    counter = 0
    try:
        for i in range(0, x):
            if (i < x):
                print(str(my_list[i]), end="")
                counter += 1
        print()
        return counter
    except Exception:
        print()
        return counter
