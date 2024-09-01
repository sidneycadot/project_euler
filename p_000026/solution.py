#! /usr/bin/env python3

"""
Problem 26: Reciprocal Cycles
=============================

Link: https://projecteuler.net/problem=26

Description
===========

A unit fraction contains in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2 = 0.5
    1/3 = 0.3
    1/4 = 0.25
    1/5 = 0.2
    1/6 = 0.1(6)
    1/7 = 0.(142857)
    1/8 = 0.125
    1/9 = 0.(1)
    1/10 = 0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""

def decimal_expansion_repeat_length(d: int):
    """Return the repeat length of the decimal expansion of 1/d."""

    remainder = 1
    prev = {}

    while True:
        remainder = (remainder * 10) % d
        if remainder in prev:
            break
        prev[remainder] = len(prev)

    return len(prev) - prev[remainder]

def main():

    (d_max, dc_max) = (None, 0)

    for d in range(1, 1000):
        dc = decimal_expansion_repeat_length(d)
        if dc > dc_max:
            (d_max, dc_max) = (d, dc)

    print("solution:", d_max)

if __name__ == "__main__":
    main()
