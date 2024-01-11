#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on
an N×N chessboard. Write a program that solves the N queens problem.

    Usage: nqueens N
        If the user called the program with the wrong number of arguments,
          print Usage: nqueens N, followed by a new line, and exit with
          the status 1
    where N must be an integer greater or equal to 4
        If N is not an integer, print N must be a number, followed by a new
          line, and exit with the status 1
        If N is smaller than 4, print N must be at least 4, followed by a
          new line, and exit with the status 1
    The program should print every possible solution to the problem
        One solution per line
        Format: see example
        You don’t have to print the solutions in a specific order
    You are only allowed to import the sys module
"""
import sys

# parse arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
n = sys.argv[1]
try:
    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
except ValueError:
    print("N must be a number")
    sys.exit(1)

# calculate valid possibilities
cols = set()
pos_x = set()  # r + c
neg_x = set()  # r - c
sol = []


def place_queen(r: int) -> None:
    """recursively place n queens"""
    if r == n:
        # we have successfully placed the n queens
        print(sol)
        return
    for c in range(n):
        if c not in cols and (r + c) not in pos_x and (r - c) not in neg_x:
            cols.add(c)
            pos_x.add(r + c)
            neg_x.add(r - c)
            sol.append([r, c])

            place_queen(r + 1)

            # bactrack - clean up after dead end or successful completion
            cols.remove(c)
            pos_x.remove(r + c)
            neg_x.remove(r - c)
            sol.remove([r, c])


place_queen(0)
