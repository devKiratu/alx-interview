#!/usr/bin/python3
"""
Algorithm for building a Pascal's triangle
"""


def getRow(prev):
    """
    Helper function for building a row in Pascal's triangle from the
    preceding row
    """
    row = []
    if len(prev) == 1:
        return [1, 1]
    row.append(1)

    i = 0
    while i < len(prev) - 1:
        nextNum = prev[i] + prev[i + 1]
        row.append(nextNum)
        i += 1
    row.append(1)
    return row


def pascal_triangle(n):
    """returns a list representation of Pascal's triangle of depth n"""
    triangle = []
    prev = []
    if n <= 0:
        return triangle
    if n >= 1:
        prev.append(1)
        triangle.append(prev)

    i = 2
    while i <= n:
        current = getRow(prev)
        triangle.append(current)
        prev = current
        i += 1
    return triangle
