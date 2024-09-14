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

from pelib import binomial

def solve() -> int:
    # We need to make 40 steps; 20 of those steps need to be to the right.
    return binomial(40, 20)

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
