#! /usr/bin/env python3

"""
Problem 48: Self Powers
=======================

Link: https://projecteuler.net/problem=48

Description
===========

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

from pelib import powermod

def main():

    modulo = 10**10
    solution = sum(powermod(k, k, modulo) for k in range(1, 1001)) % modulo
    print("solution:", solution)

if __name__ == "__main__":
    main()
