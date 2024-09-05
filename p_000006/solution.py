#! /usr/bin/env python3

"""
Problem 6: Sum Square Difference
================================

Link: https://projecteuler.net/problem=6

Description
===========

The sum of the squares of the first ten natural numbers is,

    1² + 2² + ... + 10² = 385.

The square of the sum of the first ten natural numbers is,

   (1 + 2 + ... + 10)² = 55² = 3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def solve() -> int:
    numbers = list(range(1, 101))
    sum_of_squares = sum(k**2 for k in numbers)
    square_of_sum = sum(numbers) ** 2
    return square_of_sum - sum_of_squares

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
