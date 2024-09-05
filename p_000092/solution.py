#! /usr/bin/env python3

"""
Problem 92: Square Digit Chains
===============================

Link: https://projecteuler.net/problem=92

Description
===========

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

  44 → 32 → 13 → 10 → 1 → 1
  85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop.
What is most amazing is that EVERY starting number will eventually arrive at or 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""

import functools

@functools.cache
def end_of_the_line(n: int) -> int:
    if n in (1, 89):
        return n
    n = sum(int(d)**2 for d in str(n))
    return end_of_the_line(n)

def solve() -> int:
    count = 0
    for n in range(1, 10000000):
        if end_of_the_line(n) == 89:
            count += 1
    return count

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
