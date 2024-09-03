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

def has_property(n: int) -> bool:
    k = 1
    while True:
        z = 2 * k ** 2
        if z >= n:
            return False
        if is_prime(n - z):
            return True
        k += 1

def main():
    n = 3
    while True:
        if not is_prime(n):
            if not has_property(n):
                break
        n += 2
    print("solution:", n)

if __name__ == "__main__":
    main()
