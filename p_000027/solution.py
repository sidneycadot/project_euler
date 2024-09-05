#! /usr/bin/env python3

"""
Problem 27: Quadratic Primes
============================

Link: https://projecteuler.net/problem=27

Description
===========

Euler discovered the remarkable quadratic formula:

    n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤ n ≤ 39.
However, when n=40, 40²+40+41 = 40*(40 + 1) + 41 is divisible by 41, and certainly when n=41, 41²+41+41 is clearly divisible by 41.

The incredible formula n² - 79n + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤ n ≤ 79.
The product of the coefficients, -79 and , 1601, is -126479.

Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| ≤ 1000

   where |n| is the modulus/absolute value of n
   e.g. |11| = 11 and |-4| = 4.

Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n,
starting with n=0.
"""

from pelib import is_prime

def count_generated_primes(a: int, b: int) -> int:
    n = 0
    while True:
        candidate = n ** 2 + a*n + b
        if not is_prime(candidate):
            break
        n = n + 1
    return n

def solve() -> int:

    a_max = None
    b_max = None
    count_max = 0

    for a in range(-999, +1000):
        for b in range(-1000, +1001):
            count = count_generated_primes(a, b)
            if count > count_max:
                (a_max, b_max, count_max) = (a, b, count)

    return a_max * b_max

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
