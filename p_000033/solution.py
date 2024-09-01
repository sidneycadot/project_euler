#! /usr/bin/env python3

"""
Problem 33: Digit Cancelling Fractions
======================================

Link: https://projecteuler.net/problem=33

Description
===========

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5 to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

from fractions import Fraction

def main():
    product = Fraction(1)
    for numerator in range(10, 100):
        for denominator in range(10, 100):
            if numerator < denominator:
                for cancel in range(1, 10):
                    nc = str(numerator).replace(str(cancel), "")
                    dc = str(denominator).replace(str(cancel), "")
                    if len(nc) == 1 and len(dc) == 1:
                        if numerator * int(dc) == denominator * int(nc):
                            product *= Fraction(numerator, denominator)
    solution = product.denominator
    print("solution:", solution)

if __name__ == "__main__":
    main()