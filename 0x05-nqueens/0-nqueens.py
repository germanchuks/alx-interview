#!/usr/bin/python3
"""
This script solves the N-Queens problem for a given value of N.
Usage: nqueens N
"""
import sys


if len(sys.argv) > 2 or len(sys.argv) < 2:
    print("Usage: nqueens N")
    exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    exit(1)

if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    exit(1)

n = int(sys.argv[1])


def queens(n, row=0, col=[], diag1=[], diag2=[]):
    """
    Recursively generates all possible solutions to the N-Queens problem.
    """
    if row < n:
        for i in range(n):
            if i not in col and row + i not in diag1 and row - i not in diag2:
                yield from queens(n, row + 1, col + [i], diag1 + [row + i],
                                  diag2 + [row - i])
    else:
        yield col


def solve(n):
    """
    Solves the N-Queens problem and prints all possible solutions.
    """
    solution_list = []
    row = 0
    for solution in queens(n, 0):
        for col in solution:
            solution_list.append([row, col])
            row += 1
        print(solution_list)
        solution_list = []
        row = 0


solve(n)
