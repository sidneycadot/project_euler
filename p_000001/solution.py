#! /usr/bin/env python3

"""
Problem 1: Multiples of 3 or 5
==============================

Link: https://projecteuler.net/problem=1

Description
===========

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

from pelib import gcd

def solve() -> int:
	return sum(k for k in range(1, 1000) if gcd(k, 15) != 1)

def main():
	solution = solve()
	print("solution:", solution)

if __name__ == "__main__":
	main()
