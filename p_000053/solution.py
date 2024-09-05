#! /usr/bin/env python3

"""
Problem 53: Combinatorial Selections
====================================

Link: https://projecteuler.net/problem=53

Description
===========

There are exactly ten ways of selecting three from five, 12345:

     123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, Binomial(5, 3) = 10.

In general, Binomial(n, r) = n! / (r! × (n-r)!), where r <= n, n! = n × (n-1) × ... × 3 × 2 × 1, and 0! = 1.

It is not until n = 23, that a value exceeds one-million: Binomial(23, 10) = 1144066.

How many, not necessarily distinct, values Binomial(n, 3) for 1 ≤ n ≤ 100 , are greater than one-million?
"""

import math

def solve() -> int:
    values = [math.comb(n, r) for n in range(1, 101) for r in range(n + 1)]
    return len([v for v in values if v > 1000000])

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
