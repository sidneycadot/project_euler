#! /usr/bin/env python3

"""
Problem 80: Square Root Digital Expansion
=========================================

Link: https://projecteuler.net/problem=80

Description
===========

It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is
infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square
roots.
"""

from pelib import digit_sum, floor_of_sqrt

def is_square(n: int):
    return floor_of_sqrt(n) ** 2 == n

def approximate_sqrt(n: int, digits: int):
    denominator = 10**digits
    lo = 0
    hi = n * denominator
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid ** 2 <= n * denominator ** 2:
            lo = mid
        else:
            hi = mid
    return lo

def solve() -> int:
    # We must sum the digits over the non-squares i the range (0, 1, ..., 99).
    # As defined in the problem, both the digits before and after the decimal point contribute to the "first 100 digits".
    total_digit_sum = 0
    for n in range(100):
        if not is_square(n):
            integer_part = floor_of_sqrt(n)
            digits = approximate_sqrt(n, 100 - len(str(integer_part)))
            total_digit_sum += digit_sum(digits)
    return total_digit_sum

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
