#! /usr/bin/env python3

"""
Problem 69: Totient Maximum
===========================

Link: https://projecteuler.net/problem=69

Description
===========

Euler's totient function, [sometimes called the phi function], is defined as the number of positive integers not exceeding n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than or equal to nine and relatively prime to nine, φ(9)=6.

    n     Relatively Prime    φ(n)    n/φ(n)
    2      1                  1       2
    3      1,2                2       1.5
    4      1,3                2       2
    5      1,2,3,4            4       1.25
    6      1,5                2       3
    7      1,2,3,4,5,6        6       1.1666...
    8      1,3,5,7            4       2
    9      1,2,4,5,7,8        6       1.5
   10      1,3,7,9            4       2.5

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1000000 for which n/φ(n) is a maximum.
"""

from pelib import factorize, product
from fractions import Fraction

def euler_phi(n: int) -> int:
    """Return the number of positive integers < n that are relative prime to n."""
    if n == 0:
        return 0
    return product(p ** (e - 1) * (p - 1) for (p, e) in factorize(abs(n)))

def solve() -> int:
    max_ratio_solution = max((Fraction(n, euler_phi(n)), n) for n in range(1, 1 + 1000000))
    return max_ratio_solution[1]

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
