#! /usr/bin/env python3

"""
Problem 46: Goldbach's Other Conjecture
=======================================

Link: https://projecteuler.net/problem=46

Description
===========

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

    9 =   7 + 2×1²
    15 =  7 + 2×2²
    21 =  3 + 2×3²
    25 =  7 + 2×3²
    27 = 19 + 2×2²
    33 = 31 + 2×1²

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

import itertools
from pelib import is_prime

def has_property(n: int) -> bool:
    k = 1
    while True:
        z = 2 * k ** 2
        if z >= n:
            return False
        if is_prime(n - z):
            return True
        k += 1

def solve() -> int:
    for n in itertools.count(3, 2):
        if not is_prime(n):
            if not has_property(n):
                return n

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
