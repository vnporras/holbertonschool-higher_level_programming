#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for number in enumerate(row):
            print("{:d}".format(number[1]),
                  end="" if number[0] == len(row) - 1 else " ")
        print()
