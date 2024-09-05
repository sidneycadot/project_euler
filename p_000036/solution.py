#! /usr/bin/env python3

"""
Problem 36: Double-base Palindromes
===================================

Link: https://projecteuler.net/problem=36

Description
===========

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def solve() -> int:
    return sum(k for k in range(1000000) if is_palindrome(f"{k:d}") and is_palindrome(f"{k:b}"))

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
