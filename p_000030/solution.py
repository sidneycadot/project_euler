#! /usr/bin/env python3

"""
Problem 30: Digit Fifth Powers
==============================

Link: https://projecteuler.net/problem=30

Description
===========

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1=1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def sum_of_digit_powers(n: int, exponent: int) -> int:
    return sum(int(c)**exponent for c in str(n))

def main():
    """We only need to consider numbers below a certain limit, as the sum of the fifth powers of digits is bounded by num_digits(n)*9^5
    which grows logarithmically.

    For fifth powers, since 6*9^5 == 354294, we only need to consider numbers up to that.
    """

    limit = 6*9**5

    solution = sum(k for k in range(2, limit + 1) if k == sum_of_digit_powers(k, 5))
    print("solution:", solution)

if __name__ == "__main__":
    main()
