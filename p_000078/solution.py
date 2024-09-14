#! /usr/bin/env python3

"""
Problem 78: Coin Partitions
===========================

Link: https://projecteuler.net/problem=78

Description
===========

Let p(n) represent the number of different ways in which n coins can be separated into piles.
For example, five coins can be separated into piles in exactly seven different ways, so p(5) = 7.

     OOOOO
     OOOO   O
     OOO   OO
     OOO   O   O
     OO   OO   O
     OO   O   O   O
     O   O   O   O   O

Find the least value of n for which p(n) is divisible by one million.
"""

import itertools
import functools

@functools.cache
def count_partitions(target: int, max_term: int) -> int:
    if target < 0:
        return 0
    if target == 0:
        return 1
    count = 0
    for term in range(1, max_term + 1):
        count += count_partitions(target - term, term)
    return count

def solve() -> int:
    for n in itertools.count():
        p = count_partitions(n, n)
        if p % 100000 == 0:
            return n

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
