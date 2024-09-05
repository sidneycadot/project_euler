#! /usr/bin/env python3

"""
Problem 3: Largest Prime Factor
===============================

Link: https://projecteuler.net/problem=3

Description
===========

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from pelib import factorize

def solve() -> int:
    return max(prime for (prime, exponent) in factorize(600851475143))

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
