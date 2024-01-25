#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

    Prototype: def rotate_2d_matrix(matrix):
    Do not return anything. The matrix must be edited in-place.
    You can assume the matrix will have 2 dimensions and will not be empty.
"""


def rotate_2d_matrix(matrix):
    """
    rotates a 2d matrix in place
    """
    n = len(matrix)

    # Transpose the matrix - sets each row in final position but in
    # reversed order
    for r in range(n):
        for c in range(r, n):
            matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]

    # reverse each row in the matrix
    for row in matrix:
        left = 0
        right = len(row) - 1
        while left < right:
            row[left], row[right] = row[right], row[left]
            left += 1
            right -= 1
