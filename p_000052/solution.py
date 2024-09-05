#! /usr/bin/env python3

"""
Problem 52: Permuted Multiples
==============================

Link: https://projecteuler.net/problem=52

Description
===========

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

import itertools

def digits(n: int) -> tuple:
    return tuple(sorted(c for c in str(n)))

def solve() -> int:
    for n in itertools.count(1):
        d = digits(n)
        if digits(2 * n) != d: continue
        if digits(3 * n) != d: continue
        if digits(4 * n) != d: continue
        if digits(5 * n) != d: continue
        if digits(6 * n) != d: continue
        return n

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
