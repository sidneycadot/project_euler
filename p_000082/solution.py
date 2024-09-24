#! /usr/bin/env python3

"""
Problem 81: Path Sum: Two Ways
==============================

Link: https://projecteuler.net/problem=81

Description
===========

The minimal path sum in the 5 by 5 matrix below, by starting in any cell in the left column and finishing in any cell in the right column, and only
moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

   131 673 234 103  18
   201  96 342 965 150
   630 803 746 422 111
   537 699 497 121 956
   805 732 524  37 331

Find the minimal path sum from the left column to the right column in matrix.txt
(right click and "Save Link/Target As..."), a 31K text file containing an 80 by 80 matrix.
"""

import heapq

def solve() -> int:

    m = {}
    with open("matrix.txt", "r") as fi:
        for (line_nr, line) in enumerate(fi, 1):
            for (col_nr, value_str) in enumerate(line.split(","), 1):
                value = int(value_str)
                key = (line_nr, col_nr)
                m[key] = value

    target = (80, 80)

    heap = []
    for ((r, c), value) in m.items():
        if c == 1:
            heapq.heappush(heap, (m[(r, c)], (r, c)))

    visited = set()

    while True:
        (cost, node) = heapq.heappop(heap)
        if node in visited:
            continue

        if node[1] == 80:
            return cost

        visited.add(node)

        for (dx, dy) in ((+1, 0), (0, -1), (0, +1)):
            destination = (node[0] + dy, node[1] + dx)
            step_cost = m.get(destination)
            if step_cost is None:
                continue
            heapq.heappush(heap, (cost + step_cost, destination))


def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
