#! /usr/bin/env python3

"""
Problem 4: Largest Palindrome Product
=====================================

Link: https://projecteuler.net/problem=4

Description
===========

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91×99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(n: int) -> bool:
    s = str(n)
    r = s[::-1]
    return s == r

def solve() -> int:
    max_palindrome = 0  # Assume we will beat this.
    for p in range(100, 1000):
        for q in range(100, 1000):
            n = p * q
            if is_palindrome(n):
                max_palindrome = max(max_palindrome, n)
    return max_palindrome

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
