#! /usr/bin/env python3

"""
Problem 87: Prime Power Triples
===============================

Link: https://projecteuler.net/problem=87

Description
===========

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28.
In fact, there are exactly four numbers below fifty that can be expressed in such a way:

  28 = 2**2 + 2**3 + 2**4
  33 = 3**2 + 2**3 + 2**4
  49 = 5**2 + 2**3 + 2**4
  47 = 2**2 + 3**3 + 2**4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
"""

import functools

from pelib import prime_sieve

primes = prime_sieve(10000)
prime_squares = frozenset(p*p for p in primes)

@functools.cache
def can_be_expressed_as_prime_power_sum_with_exponents_2_to_e(n: int, e: int) -> bool:

    if e == 2:
        return n in prime_squares

    for p in primes:
        pe = p ** e
        if pe > n:
            return False
        if can_be_expressed_as_prime_power_sum_with_exponents_2_to_e(n - pe, e - 1):
            return True

def solve() -> int:
    count = 0
    for n in range(50000000):
        if can_be_expressed_as_prime_power_sum_with_exponents_2_to_e(n, 4):
            count += 1
    return count

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
