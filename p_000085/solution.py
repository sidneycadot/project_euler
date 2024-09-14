#! /usr/bin/env python3

"""
Problem 85: Counting Rectangles
===============================

Link: https://projecteuler.net/problem=85

Description
===========

By counting carefully it can be seen that a rectangular grid measuring 3 by 2 contains eighteen rectangles:

    +--+--+--+    +--+--+--+     +--+--+--+
    |XX|  |  |    |XXXXX|  |     |XXXXXXXX|
    +--+--+--+    +--+--+--+     +--+--+--+
    |  |  |  |    |  |  |  |     |  |  |  |
    +--+--+--+    +--+--+--+     +--+--+--+
        6             4              2

    +--+--+--+    +--+--+--+     +--+--+--+
    |XX|  |  |    |XXXXX|  |     |XXXXXXXX|
    +XX+--+--+    +XXXXX|--+     +XXXXXXXX+
    |XX|  |  |    |XXXXX|  |     |XXXXXXXX|
    +--+--+--+    +--+--+--+     +--+--+--+
        3             4              1

Although there exists no rectangular grid that contains exactly two million rectangles, find the area of the grid with the nearest solution.
Find the least value of n for which p(n) is divisible by one million.
"""

import itertools
import functools

def count_rectangles_in_grid(h: int, v: int) -> int:
    count = 0
    for xs in range(1, h + 1):
        for ys in range(1, v + 1):
            count += (h - xs + 1) * (v - ys + 1)
    return count

def count_rectangles_in_grid_v2(h: int, v: int) -> int:
    return h * (h + 1) * v * (v + 1) // 4

def solve() -> int:
    best_score = 10**100
    best_area = None
    for h in range(500):
        for v in range(h, 500):
            c = count_rectangles_in_grid_v2(h, v)
            score = abs(c - 2000000)
            if score < best_score:
                best_score = score
                best_area = h * v
    return best_area

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
