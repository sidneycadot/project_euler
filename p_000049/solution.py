#! /usr/bin/env python3

"""
Problem 49: Prime Permutations
==============================

Link: https://projecteuler.net/problem=49

Description
===========

The arithmetic sequence, 1487, 4717, 8147, in which each of the terms increases by 3330, is unusual in two ways:
(i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

import functools

@functools.cache
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

def main():
    for p in range(1000, 10000):
        if not is_prime(p):
            continue
        for q in range(p + 1, 10000):
            if not is_prime(q):
                continue
            r = q + q - p
            if not r < 10000:
                continue
            if not is_prime(r):
                continue
            pd = sorted(str(p))
            qd = sorted(str(q))
            rd = sorted(str(r))
            if not (pd == qd == rd):
                continue
            solution = str(p) + str(q) + str(r)
            if solution != "148748178147":
                break
    print("solution:", solution)

if __name__ == "__main__":
    main()
