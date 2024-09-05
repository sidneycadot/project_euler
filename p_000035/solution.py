#! /usr/bin/env python3

"""
Problem 35: Circular Primes
===========================

Link: https://projecteuler.net/problem=35

Description
===========

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 73, 79, and 97.

How many circular primes are there below one million?
"""

from pelib import is_prime

def is_circular_prime(n: int) -> bool:
    if not is_prime(n):
        return False

    ns = str(n)
    for k in range(len(ns) - 1):
        ns = ns[1:] + ns[0]
        if not is_prime(int(ns)):
            return False

    return True

def solve() -> int:
    count = 0
    for k in range(1000000):
        if is_circular_prime(k):
            count += 1
    return count

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
