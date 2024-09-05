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

from pelib import prime_sieve

def main():
    solution = sum(prime_sieve(2000000))
    print("solution:", solution)

if __name__ == "__main__":
    main()
