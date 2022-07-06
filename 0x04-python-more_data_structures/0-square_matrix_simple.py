#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    '''Function that computes the square value of all integers of a matrix.'''
    return ([list(map(lambda num: num * num, i)) for i in matrix])
