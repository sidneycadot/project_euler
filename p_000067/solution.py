#! /usr/bin/env python3

"""
Problem 67: Maximum Path Sum II
===============================

Link: https://projecteuler.net/problem=67

Description
===========

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 3 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with
one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2**99 altogether!
If you could check one trillion (10**12) routes every second it would take over twenty billion years to check them all.
There is an efficient algorithm to solve it. ;o)
"""

import functools

class TriangleLookup:
    def __init__(self, entries):
        self._entries = list(entries)
    def __call__(self, r: int, c: int):
        offset = r * (r + 1) // 2
        index = offset + c
        return self._entries[index]

@functools.cache
def max_route(triangle: TriangleLookup, r: int, c: int):
    if r == 0 and c == 0:
        return triangle(r, c)
    if c == 0:
        return triangle(r, c) + max_route(triangle, r - 1, c)
    if c == r:
        return triangle(r, c) + max_route(triangle, r - 1, c - 1)
    return triangle(r, c) + max(max_route(triangle, r - 1, c - 1), max_route(triangle, r - 1, c))

def solve() -> int:

    with open("triangle.txt", "r") as fi:
        triangle_string = fi.read()

    triangle = TriangleLookup(map(int, triangle_string.split()))

    return max(max_route(triangle, 99, c) for c in range(100))

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
