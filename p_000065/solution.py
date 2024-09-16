#! /usr/bin/env python3

"""
Problem 65: Convergents of e
============================

Link: https://projecteuler.net/problem=65

Description
===========

The square root of can be written as an infinite continued fraction.

    sqrt(2) = 1 + 1 / (2 + 1 / (2 + 1 / (2 + 1 / (2 + 1 / (2 + ...)))))

The infinite continued fraction sqrt(2) can be written, sqrt(2) = [1;(2)], (2) indicates that 2 repeats ad infinitum. In a similar way,

    sqrt(23) = [4;(1,3,1,8)]

It turns out that the sequence of partial values of continued fractions for square roots provide the best rational approximations.
Let us consider the convergents for sqr(2).

    1 + 1/2 = 3/2
    1 + 1/(2 + 1/2) = 7/5
    1 + 1/(2+1/(2+1/2)) = 17/12
    1 + 1/(2+1/(2+1/(2+1/2))) = 41/29

Hence the sequence of the first ten convergents for sqrt(2) are:

    1, 3/2, 7/5, 17/2, 41/29. 99/70. 239/169. 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant,

    e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, ..., 1, 2k, 1, ...].

The first ten terms in the sequence of convergents for e are:

    2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...

The sum of digits in the numerator of the 10th convergent is 1 + 4 + 5 + 7 = 17..

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
"""

from fractions import Fraction

from pelib import digit_sum

def cf_e():
    yield 2
    k = 2
    while True:
        yield 1
        yield k
        yield 1
        k += 2

def continued_fraction_convergent(generator, n: int) -> Fraction:
    value = Fraction(next(generator))
    if n == 0:
        return value
    else:
        return value + Fraction(1, continued_fraction_convergent(generator, n - 1))

def solve() -> int:
    convergent = continued_fraction_convergent(cf_e(), 99)
    return digit_sum(convergent.numerator)

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
