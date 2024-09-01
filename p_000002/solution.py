#! /usr/bin/env python3

"""
Problem 2: Even Fibonacci Numbers
=================================

Link: https://projecteuler.net/problem=2

Description
===========

Each new term in the Fibonacci sequence is generated by adding the previous two terms.
By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

def main():
    fib = [1, 2]
    while True:
        next_entry = fib[-2] + fib[-1]
        if next_entry > 4000000:
            break
        fib.append(next_entry)

    solution = sum(f for f in fib if f % 2 == 0)
    print("solution:", solution)

if __name__ == "__main__":
    main()
