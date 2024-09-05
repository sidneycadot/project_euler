#! /usr/bin/env python3

"""
Problem 32: Pandigital Products
===============================

Link: https://projecteuler.net/problem=32

Description
===========

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number,
15324, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39×186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

import itertools

def solve() -> int:
    achievable_products = set()
    for permutation in itertools.permutations(range(1, 10)):
        xs = "".join(map(str, permutation))
        assert len(xs) == 9
        for i1 in range(1, 7):
            x1 = int(xs[:i1])
            for i2 in range(i1 + 1, 8):
                x2 = int(xs[i1:i2])
                x3 = int(xs[i2:])
                if x1 * x2 == x3:
                    achievable_products.add(x3)
    return sum(achievable_products)

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
