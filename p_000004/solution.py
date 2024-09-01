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

def main():
    palindromes = set()
    for p in range(100, 1000):
        for q in range(100, 1000):
            n = p * q
            if is_palindrome(n):
                palindromes.add(n)

    solution = max(palindromes)
    print("solution:", solution)

if __name__ == "__main__":
    main()
