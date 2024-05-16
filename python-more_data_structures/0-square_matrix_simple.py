#!/usr/bin/python3

def square(number):
    return number * number

def square_matrix_simple(matrix=[]):
    result = []

    for i in matrix:
        result.append(list(map(square, i)))
    return result
