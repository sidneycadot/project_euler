#! /usr/bin/env python3

"""
Problem 76: Counting Summations
===============================

Link: https://projecteuler.net/problem=76

Description
===========

It is possible to write five as a sum in exactly six different ways:

    4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
"""

import functools

@functools.cache
def count_sums(target: int, max_term: int) -> int:
    if target < 0:
        return 0
    if target == 0:
        return 1
    count = 0
    for term in range(1, max_term + 1):
        count += count_sums(target - term, term)
    return count

def solve() -> int:
    return count_sums(100, 99)

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
