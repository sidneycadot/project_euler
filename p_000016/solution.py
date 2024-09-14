#! /usr/bin/env python3

"""
Problem 16: Power Digit Sum
===========================

Link: https://projecteuler.net/problem=16

Description
===========

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""

from pelib import digit_sum

def solve() -> int:
    return digit_sum(2**1000)

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
