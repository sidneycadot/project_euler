#! /usr/bin/env python3

"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a≠b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def divisors(n: int) -> list[int]:
    return [d for d in range(1, n) if n % d == 0]

def is_amicable_number(n: int) -> bool:
    q = sum(divisors(n))
    return (q != n) and sum(divisors(q)) == n

def main():

    solution = sum(k for k in range(10000) if is_amicable_number(k))
    print("solution:", solution)

if __name__ == "__main__":
    main()
