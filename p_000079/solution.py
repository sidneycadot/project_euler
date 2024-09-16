#! /usr/bin/env python3

"""
Problem 79: Passcode Derivation
===============================

Link: https://projecteuler.net/problem=79

Description
===========

A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was
531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown
length.
"""

import itertools
import functools

def is_compatible(passcode: str, successful_login: str) -> bool:
    n1 = len(passcode)
    n2 = len(successful_login)

    i1 = n1 - 1
    i2 = n2 - 1

    while i1 >= i2:
        if passcode[i1] == successful_login[i2]:
            if i2 == 0:
                return True
            i2 -= 1
        i1 -= 1

    return False

def solve() -> int:
    with open("keylog.txt", "r") as fi:
        successful_logins = sorted(set(fi.read().split()))

    for passcode_int in itertools.count():
        passcode = str(passcode_int)
        if all(is_compatible(passcode, successful_login) for successful_login in successful_logins):
            return passcode_int
def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
