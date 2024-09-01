#! /usr/bin/env python3

"""
Problem 9: Special Pythagorean Triplet
======================================

Link: https://projecteuler.net/problem=9

Description
===========

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

    a² + b² = c².

For example, 3² + 4² = 9 + 16 = 25 = 5².

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

Find the product abc.
"""

def generate_pythagorean_triplets():
    c = 0
    while True:
        for b in range(c):
            for a in range(b):
                if a ** 2 + b ** 2 == c ** 2:
                    yield (a, b, c)
        c += 1

def main():

    for (a, b, c) in generate_pythagorean_triplets():
        if a + b + c == 1000:
            break
    solution = a * b * c
    print("solution:", solution)

if __name__ == "__main__":
    main()
