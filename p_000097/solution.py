#! /usr/bin/env python3

"""
Problem 97: Large Non-Mersenne Prime
====================================

Link: https://projecteuler.net/problem=97

Description
===========

The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 2**6972593-1;
it contains exactly 2098960 digits. Subsequently other Mersenne primes, of the form 2**p-1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2357207 digits: 28433×2**7830457+1.

Find the last ten digits of this prime number.
"""

from pelib import powermod

def solve() -> int:
    modulo = 10**10
    return (28433 * powermod(2, 7830457, modulo) + 1) % modulo

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
