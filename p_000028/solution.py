#! /usr/bin/env python3

"""
Problem 28: Number Spiral Diagonals
===================================

Link: https://projecteuler.net/problem=28

Description
===========

Starting with the number and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

def spiral_diagonal_sum(side: int) -> int:
    """Return the sum of the numbers on the diagonals of a side×side spiral.
       This formula was derived using Mathematica.
    """
    return (-9 + side*(8 + side*(3 + 4*side))) // 6

def solve() -> int:
    return spiral_diagonal_sum(1001)

def main():
    solution = solve()
    return solution

if __name__ == "__main__":
    main()
