#! /usr/bin/env python3

"""
Problem 89: Roman Numerals
==========================

Link: https://projecteuler.net/problem=89

Description
===========

For a number written in Roman numerals to be considered valid there are basic rules which must be followed. Even though the rules allow some numbers
to be expressed in more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

    IIIIIIIIIIIIIIII
    VIIIIIIIIIII
    VVIIIIII
    XIIIIII
    VVVI
    XVI

However, according to the rules only XIIIIII and XVI are valid, and the last example is considered to be the most efficient,
as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal,
Roman numerals; see About... Roman Numerals for the definitive rules for this problem.

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
"""

import functools

from pelib import prime_sieve

primes = prime_sieve(10000)
prime_squares = frozenset(p*p for p in primes)

@functools.cache
def can_be_expressed_as_prime_power_sum_with_exponents_2_to_e(n: int, e: int) -> bool:

    if e == 2:
        return n in prime_squares

    for p in primes:
        pe = p ** e
        if pe > n:
            return False
        if can_be_expressed_as_prime_power_sum_with_exponents_2_to_e(n - pe, e - 1):
            return True

def solve() -> int:
    count = 0
    for n in range(50000000):
        if can_be_expressed_as_prime_power_sum_with_exponents_2_to_e(n, 4):
            count += 1
    return count

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
