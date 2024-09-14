#! /usr/bin/env python3

"""
Problem 14: Longest Collatz Sequence
====================================

Link: https://projecteuler.net/problem=14

Description
===========

The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import functools

@functools.cache
def collatz_sequence_length(n: int) -> int:
    assert n >= 1
    if n == 1:
        return 1
    return 1 + collatz_sequence_length(n // 2 if n % 2 == 0 else 3 * n + 1)

def solve() -> int:
    n_max = None
    nlen_max = 0
    for n in range(1, 1000000):
        nlen = collatz_sequence_length(n)
        if nlen > nlen_max:
            n_max = n
            nlen_max = nlen
    return n_max

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
