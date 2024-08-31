#! /usr/bin/env python3

import functools

"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

@functools.cache
def walks(x: int, y: int) -> int:
    if x == 0 and y == 0:
        return 1
    if x == 0:
        return walks(x, y - 1)
    if y == 0:
        return walks(x - 1, y)
    return walks(x, y - 1) + walks(x - 1, y)


def main():
    solution = walks(20, 20)
    print("solution:", solution)


if __name__ == "__main__":
    main()
