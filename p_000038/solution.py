#! /usr/bin/env python3

"""
Problem 38: Pandigital Multiples
================================

Link: https://projecteuler.net/problem=38

Description
===========

Take the number 192 and multiply it by each of 1, 2, and 3:

    192×1 = 192
    192×2 = 384
    192×3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1, 2, 3).

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1, 2, 3, 4, 5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1, 2, ..., n) where n > 1?
"""

import itertools

def is_pandigital_multiple(n: int):
    ns = str(n)
    for k in range(1, len(ns)):
        ms = ns[:k]
        m = int(ms)
        z = 1
        while True:
            z += 1
            ms += str(z * m)
            if len(ms) > len(ns):
                break
            if ms == ns:
                return True

def solve() -> int:
    for candidate in itertools.permutations(range(9, 0, -1)):
        candidate = int("".join(map(str, candidate)))
        if is_pandigital_multiple(candidate):
            return candidate

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
