#! /usr/bin/env python3

"""
Problem 50: Consecutive Prime Sum
=================================

Link: https://projecteuler.net/problem=50

Description
===========

The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""

import itertools
from pelib import is_prime_cached as is_prime

def main():

    primes = [p for p in range(1000000) if is_prime(p)]
    prime_sum = list(itertools.accumulate(primes, initial=0))

    max_range_sums = []
    max_range_size = 0

    for i1 in range(len(primes)):
        for i2 in range(i1, len(primes)):
            range_size = i2 - i1
            if range_size < max_range_size:
                continue
            range_sum = prime_sum[i2] - prime_sum[i1]
            if range_sum >= 1000000:
                break
            if is_prime(range_sum):
                if range_size > max_range_size:
                    max_range_size = range_size
                    max_range_sums.clear()
                max_range_sums.append(range_sum)

    assert len(max_range_sums) == 1
    solution = max_range_sums[0]
    print("solution:", solution)

if __name__ == "__main__":
    main()
