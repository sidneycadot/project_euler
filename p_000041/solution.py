#! /usr/bin/env python3

"""
Problem 41: Pandigital Prime
============================

Link: https://projecteuler.net/problem=41

Description
===========

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example 2143, is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import itertools
from pelib import is_prime

def generate_candidates():
    # Generate candidates in descending order.
    for n in range(9, 0, -1):
        descending_digits = range(n, 0, -1)
        if sum(descending_digits) % 3 == 0:
            # All generated pandigitals would be divisible by three.
            # We can safely skip this n.
            continue
        for permutation in itertools.permutations(descending_digits):
            yield int("".join(map(str, permutation)))

def solve() -> int:
    for p in generate_candidates():
        if is_prime(p):
            return p

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
