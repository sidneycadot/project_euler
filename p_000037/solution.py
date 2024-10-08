#! /usr/bin/env python3

"""
Problem 37: Truncatable Primes
==============================

Link: https://projecteuler.net/problem=37

Description
===========

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE:
2, 3, 5, and 7 are not considered to be truncatable primes.
"""

from pelib import is_prime_cached as is_prime

def is_truncatable_prime(n: int):
    if not is_prime(n):
        return False
    ns = str(n)
    for k in range(1, len(ns)):
        if not is_prime(int(ns[:k])):
            return False
        if not is_prime(int(ns[-k:])):
            return False
    return True

def solve() -> int:
    # We use the given hint that there are precisely 11 truncatable primes.
    truncatable_primes = []
    candidate = 10
    while len(truncatable_primes) != 11:
        while not is_truncatable_prime(candidate):
            candidate += 1
        truncatable_primes.append(candidate)
        candidate += 1

    return sum(truncatable_primes)

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
