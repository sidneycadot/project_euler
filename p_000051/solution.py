#! /usr/bin/env python3

"""
Problem 51: Prime Digit Replacements
====================================

Link: https://projecteuler.net/problem=51

Description
===========

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten
generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit,
is part of an eight prime value family.
"""

import itertools

def test_prime(n: int) -> bool:
    ns = [c for c in str(n)]
    for (i1, i2) in itertools.combinations(range(len(ns)+1), 2):
        for d in "0123456789":
            ns[i1:i2] = d
            value = ns

def solve() -> int:
    return -1
    #for p in range(56000, 57000):
    #    test_prime(p)

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
