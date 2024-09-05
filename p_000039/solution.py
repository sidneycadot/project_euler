#! /usr/bin/env python3

"""
Problem 39: Integer Right Triangles
===================================

Link: https://projecteuler.net/problem=39

Description
===========

If p is the perimeter of a right angle triangle with integral length sides, {a, b, c}, there are exactly three solutions for p = 120.

    {20, 48, 52}, {24, 45, 51}, {30, 40, 50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

import itertools

def find_solutions(p: int):
    solutions = []
    for a in range(1, p + 1):
        bn = (p - 2 * a) * p
        cn = 2*a**2 + p**2 - 2*a*p

        if bn <= 0 or cn <= 0:
            continue

        denom = 2 * (p - a)
        if bn % denom != 0 or cn % denom != 0:
            continue

        b = bn // denom
        c = cn // denom

        if not 0 < a < b < c:
            continue

        solutions.append((a, b, c))

    return solutions

def solve() -> int:
    p_max = None
    p_max_value = 0
    for p in range(1000):
        sols = find_solutions(p)
        p_value = len(sols)
        if p_value > p_max_value:
            p_max = p
            p_max_value = p_value
    return p_max

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
