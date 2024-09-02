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

def is_prime(n: int) -> bool:
    """Check if the given number is a prime, by trial division."""

    if n < 2:
        return False

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

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

def main():
    for p in generate_candidates():
        if is_prime(p):
            break
    else:
        p = None
    print("solution:", p)

if __name__ == "__main__":
    main()
