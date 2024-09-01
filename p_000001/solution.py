#! /usr/bin/env python3

"""
Problem 1: Multiples of 3 or 5
==============================

Link: https://projecteuler.net/problem=1

Description
===========

If we list all the natural numbers below that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

def is_multiple_of_3_or_5(n: int):
	return (n % 3 == 0) or (n % 5 == 0)

def main():
	problem_size = 1000
	solution = sum(k for k in range(1, problem_size) if is_multiple_of_3_or_5(k))
	print("solution:", solution)

if __name__ == "__main__":
	main()
