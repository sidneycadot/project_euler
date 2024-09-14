#! /usr/bin/env python3

"""
Problem 34: Digit Factorials
============================

Link: https://projecteuler.net/problem=34

Description
===========

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 == 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""

from pelib import factorial

def is_curious(n: int):
    return sum(factorial(int(c)) for c in str(n)) == n

def solve() -> int:
    # From eight digits onwards, the minimum value an n-digit number can have exceeds the maximum value attainable by multiplying its digits.
    return sum(n for n in range(3, 10000000) if is_curious(n))

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
