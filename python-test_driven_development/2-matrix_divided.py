#!/usr/bin/python3

def matrix_divided(matrix, div):
    """Divide all elements of a matrix"""

    if type(matrix) is not list:
        """Raise an error if matrix is not a list"""
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    if len(set(len(row) for row in matrix)) != 1:
        """Raise an error if the matrix is not a rectangle"""
        raise TypeError("Each row of the matrix must have the same size")
    
    if not isinstance(div, (int, float)):
        """Raise an error if div is not a number"""
        raise TypeError("div must be a number")
    
    if div == 0:
        """Raise an error if div is 0"""
        raise ZeroDivisionError("division by zero")
    
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matrix
