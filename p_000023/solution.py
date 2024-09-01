#! /usr/bin/env python3

"""
Problem 23: Non-Abundant Sums
=============================

Link: https://projecteuler.net/problem=23

Description
===========

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as
the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import itertools

def divisors(n: int) -> list[int]:
    return [d for d in range(1, n) if n % d == 0]

def is_abundant(n: int) -> bool:
    return sum(divisors(n)) > n

def main():
    abundant_numbers = [k for k in range(28124) if is_abundant(k)]

    can_be_written_as_sum_of_two_abundant_numbers = set(sum(zz) for zz in itertools.product(abundant_numbers, repeat=2))

    all_numbers =  set(range(1, 28124))

    cannot_be_written_as_sum_of_two_abundant_numbers = all_numbers - can_be_written_as_sum_of_two_abundant_numbers

    solution = sum(cannot_be_written_as_sum_of_two_abundant_numbers)
    print("solution:", solution)

if __name__ == "__main__":
    main()
