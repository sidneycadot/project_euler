#! /usr/bin/env python3

"""
Problem 7: 10001st Prime
========================

Link: https://projecteuler.net/problem=7

Description
===========

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

from pelib import next_prime

def solve() -> int:
    p = 0
    for c in range(10001):
        p = next_prime(p)
    return p

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
