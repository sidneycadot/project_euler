#! /usr/bin/env python3

"""
Problem 99: Largest Exponential
===============================

Link: https://projecteuler.net/problem=99

Description
===========

Comparing two numbers written in index form like 2**1 and 3**7 is not difficult, as any calculator would confirm that

    2**11 = 2048 < 3**7 = 2187

However, confirming that 632382**518061 > 519432**525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line,
determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
"""

import math

def solve() -> int:
    with open("base_exp.txt") as fi:
        max_index = None
        max_log_value = 0.0
        for (index, line) in enumerate(fi, 1):
            (base, exponent) = map(int,line.split(","))
            log_value = exponent * math.log(base)
            if log_value > max_log_value:
                max_log_value = log_value
                max_index = index
        return max_index

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
