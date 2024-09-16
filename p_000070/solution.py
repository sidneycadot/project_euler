#! /usr/bin/env python3

"""
Problem 70: Totient Permutation
===========================

Link: https://projecteuler.net/problem=70

Description
===========

Euler's totient function, φ(n) [sometimes called the phi function], is defined as the number of positive integers not exceeding n which are
relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than or equal to nine and relatively prime to nine, φ(9)=6.

Find the value of n ≤ 1000000 for which n/φ(n) is a maximum.

Interestingly, φ(87109) = 79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and the ratio φ/f(n) produces a minimum.
"""

from pelib import euler_phi
from fractions import Fraction

def digits(n):
    while n != 0:
        yield n % 10
        n //= 10

def is_permutation(n1: int, n2: int) -> bool:
    return sorted(digits(n1)) == sorted(digits(n2))

def solve() -> int:
    min_n = None
    min_fraction = None
    for n in range(2, 10**7):
        phi = euler_phi(n)
        if is_permutation(n, phi):
            current_fraction = Fraction(n, phi)
            if min_fraction is None or current_fraction < min_fraction:
                min_n = n
                min_fraction = current_fraction
                print(n, euler_phi(n), current_fraction)
    return min_n

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
