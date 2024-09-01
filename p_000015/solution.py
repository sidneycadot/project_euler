#! /usr/bin/env python3

"""
Problem 15: Lattice Paths
=========================

Link: https://projecteuler.net/problem=15

Description
===========

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import functools

@functools.cache
def walks(x: int, y: int) -> int:
    if x == 0 and y == 0:
        return 1
    if x < 0 or y < 0:
        return 0
    return walks(x, y - 1) + walks(x - 1, y)

def main():
    solution = walks(20, 20)
    print("solution:", solution)

if __name__ == "__main__":
    main()
