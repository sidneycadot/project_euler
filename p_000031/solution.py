#! /usr/bin/env python3

"""
Problem 31: Coin Sums
=====================

Link: https://projecteuler.net/problem=31

Description
===========

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?
"""

def generate_solutions(coins, target: int):
    if target == 0:
        yield ()
    else:
        if len(coins) > 0 and coins[0] <= target:
            # Return solutions with the smallest coin included.
            yield from ((coins[0], ) + sub_solution for sub_solution in generate_solutions(coins, target - coins[0]))
            # Return solutions with the smallest coin *not* included.
            yield from generate_solutions(coins[1:], target)

def solve() -> int:
    coins = (1, 2, 5, 10, 20, 50, 100, 200)
    return len(list(generate_solutions(coins, 200)))

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
