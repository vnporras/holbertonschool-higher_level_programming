#!/usr/bin/python3
import sys

def add_arguments(args):
    add  = sum(int(arg) for arg in args)
    return add

if __name__ == "__main__":
    arguments = sys.argv[1:]
    result = add_arguments(arguments)
    print(result)
