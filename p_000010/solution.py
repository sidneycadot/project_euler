#! /usr/bin/env python3

"""
Problem 10: Summation of Primes
===============================

Link: https://projecteuler.net/problem=10

Description
===========

The sum of the primes below 10 is 2 + 3 + 5 + 7 == 17.

Find the sum of all the primes below two million.
"""

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
    solution = sum(p for p in range(2000000) if is_prime(p))
    print("solution:", solution)

if __name__ == "__main__":
    main()
