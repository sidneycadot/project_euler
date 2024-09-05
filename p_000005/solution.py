#! /usr/bin/env python3

"""
Problem 5: Smallest Multiple
============================

Link: https://projecteuler.net/problem=5

Description
===========

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def gcd(a: int, b: int) -> int:

    while a != 0:
        (a, b) = (b % a, a)
    return b

def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)

def solve() -> int:
    result = 1
    for k in range(1, 21):
        result = lcm(result, k)
    return result

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
