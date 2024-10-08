#! /usr/bin/env python3

"""
Problem 44: Pentagon Numbers
============================

Link: https://projecteuler.net/problem=44

Description
===========

Pentagonal numbers are generated by the formula, P[n] = n(3n-1)/2. The first ten pentagonal numbers are:

     1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P[4] + P[7] == 22 + 70 == 92 == P[8]. However, their difference, 770 - 22 == 48, is not pentagonal.

Find the pair of pentagonal numbers, P[j] and P[k], for which their sum and difference are pentagonal and D=|P[k]-P[j]| is minimised;
what is the value of D?
"""

from pelib import generate_pentagonal_numbers, is_pentagonal_number

def find_pentagonal_pair():
    # Find a pentagonal pair whose difference and sum is also pentagonal.
    for difference in generate_pentagonal_numbers():
        prev_a = None
        for a in generate_pentagonal_numbers():
            if prev_a is not None:
                if a - prev_a > difference:
                    break
            prev_a = a
            b =  a + difference
            if not is_pentagonal_number(b):
                continue
            if is_pentagonal_number(a + b):
                return (a, b)

def solve() -> int:
    # NOTE: This solver is very slow; the run takes approximately 15 minutes!
    (a, b) = find_pentagonal_pair()
    return b - a

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
