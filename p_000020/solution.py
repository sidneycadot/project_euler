#! /usr/bin/env python3

"""
Problem 20: Factorial Digit Sum
===============================

Link: https://projecteuler.net/problem=20

Description
===========

n! means n×(n - 1)×...×3×2×1.

For example, 10! = 10×9×...×3×2×1 = 3628800, and the sum of the digits in the number 10! is 3+6+2+8+8+0+0=27.

Find the sum of the digits in the number 100!.
"""

from pelib import factorial, digit_sum

def solve() -> int:
    return digit_sum(factorial(100))

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
