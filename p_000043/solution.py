#! /usr/bin/env python3

"""
Problem 43: Sub-string Divisibility
===================================

Link: https://projecteuler.net/problem=43

Description
===========

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d[1] be the 1st digit, be the 2nd digit, and so on. In this way, we note the following:

* d[2]d[3]d[4] = 406 is divisible by 2.
* d[3]d[4]d[5] = 063 is divisible by 3.
* d[4]d[5]d[6] = 635 is divisible by 5.
* d[5]d[6]d[7] = 357 is divisible by 7.
* d[6]d[7]d[8] = 572 is divisible by 11.
* d[7]d[8]d[9] = 728 is divisible by 13.
* d[8]d[9]d[10] = 289 is divisible by 17.

Find the sum of all 0 to 0 pandigital numbers with this property.
"""

import itertools

def main():
    # The problem statement does not mention if numbers with a leading zero are to be considered.
    # It doesn't matter in the end; no such numbers have the described propery.

    solution = 0

    digits = range(0, 10)
    for permutation in itertools.permutations(digits):

        ns = "".join(str(digit) for digit in permutation)

        if int(ns[1:4]) % 2 != 0: continue
        if int(ns[2:5]) % 3 != 0: continue
        if int(ns[3:6]) % 5 != 0: continue
        if int(ns[4:7]) % 7 != 0: continue
        if int(ns[5:8]) % 11 != 0: continue
        if int(ns[6:9]) % 13 != 0: continue
        if int(ns[7:10]) % 17 != 0: continue

        solution += int(ns)

    print("solution:", solution)

if __name__ == "__main__":
    main()
