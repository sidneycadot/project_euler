#! /usr/bin/env python3

"""
Problem 56: Powerful Digit Sum
==============================

Link: https://projecteuler.net/problem=56

Description
===========

A googol (10**100) is a massive number: one followed by one-hundred zeros; 100**100 is almost unimaginably large: one followed by two-hundred zeros.
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a**b, where a,b < 100, what is the maximum digital sum?
"""

import itertools

from pelib import digit_sum

def solve() -> int:
    return max(digit_sum(a**b) for (a, b) in itertools.product(range(100), repeat=2))

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
