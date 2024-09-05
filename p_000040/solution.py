#! /usr/bin/env python3

"""
Problem 40: Champernowne's Constant
===================================

Link: https://projecteuler.net/problem=40

Description
===========

An irrational decimal fraction is created by concatenating the positive integers:

    0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If d[n] represents the nth digit of the fractional part, find the value of the following expression.

    d[1] × d[10] × d[100] × d[1000] × d[10000] × d[100000] × d[1000000]
"""

def solve() -> int:

    s_join = ["."]

    k = 1
    length = 0
    while length < 1000000:
        s = str(k)
        s_join.append(s)
        length += len(s)
        k += 1

    d = "".join(s_join)

    return int(d[1]) * int(d[10]) * int(d[100]) * int(d[1000]) * int(d[10000]) * int(d[100000]) * int(d[1000000])

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
