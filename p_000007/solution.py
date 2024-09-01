#! /usr/bin/env python3

"""
Problem 7: 10001st Prime
========================

Link: https://projecteuler.net/problem=7

Description
===========

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the6 th prime is 13.

What is the 10001st prime number?
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

def main():
    c = 0
    p = 0
    while True:
        while not is_prime(p):
            p += 1
        c += 1
        if c == 10001:
            break
        p += 1

    print("solution:", p)

if __name__ == "__main__":
    main()
