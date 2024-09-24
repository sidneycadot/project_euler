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

def solve() -> int:
    # The maximum sum-of-digit-factorials for a k-digit number is (9!)*k == 362880*k.
    # The minimum value of a k-digit number is 10**(k-1).
    # From 8 digits onwards, the minimum value of the number exceeds the sum-of-digit-factorials
    # that can be reached; therefore, we only need to test numbers below 10**8.

    digit_factorial = dict((str(d), factorial(d)) for d in range(10))

    return sum(n for n in range(10, 10000000) if sum(digit_factorial[c] for c in str(n)) == n)

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
