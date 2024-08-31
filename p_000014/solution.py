#! /usr/bin/env python3

"""
The following iterative sequence is defined for the set of positive integers:

    n → n/2 (n is even)
    n → 3n+1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def collatz(n: int) -> int:
    assert n >= 1
    r = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        r += 1
    return r

def main():
    n_max = None
    nc_max = 0
    for n in range(1, 1000000):
        nc = collatz(n)
        if nc > nc_max:
            n_max = n
            nc_max = nc
    print("solution:", n_max)


if __name__ == "__main__":
    main()
