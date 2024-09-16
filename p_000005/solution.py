#! /usr/bin/env python3

"""
Problem 5: Smallest Multiple
============================

Link: https://projecteuler.net/problem=5

Description
===========

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

from pelib import lcm

def solve() -> int:
    return lcm(*range(1, 21))

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
