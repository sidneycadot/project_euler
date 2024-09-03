#! /usr/bin/env python3

"""
Problem 47: Distinct Prime Factors
==================================

Link: https://projecteuler.net/problem=47

Description
===========

The first two consecutive numbers to have two distinct prime factors are:

  14 = 2×7
  15 = 3×5

The first three consecutive numbers to have three distinct prime factors are:

  644=2²×7×23
  645=3×5×43
  646=2×17×19

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

def factorize(n: int) -> list[tuple[int, int]]:
    """Returns the factorization of the argument as a list of (prime, exponent) pairs."""
    assert n >= 1
    factors = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            e += 1
            n //= p
        if e != 0:
            factors.append((p, e))
        p += 1
    if n != 1:
        factors.append((n, 1))
    return factors

def main():

    consecutive = 0
    n = 1
    while True:
        if len(factorize(n)) == 4: # number of prime factors
            consecutive += 1
            if consecutive == 4: # count of consecutive numbers with the sought number of prime factors.
                break
        else:
            consecutive = 0
        n += 1

    solution = n - consecutive + 1
    print("solution:", solution)

if __name__ == "__main__":
    main()
