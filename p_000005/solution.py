#! /usr/bin/env python3

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1to 20?
"""

def gcd(a: int, b: int) -> int:

    while a != 0:
        (a, b) = (b % a, a)
    return b

def lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)


def main():
    solution = 1
    for k in range(1, 21):
        solution = lcm(solution, k)
    print("solution:", solution)

if __name__ == "__main__":
    main()
