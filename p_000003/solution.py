#! /usr/bin/env python3

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def factorize(n: int) -> list[int]:
    assert n >= 0
    if n < 2:
        return [n]
    primes = []
    p = 2
    while p * p <= n:
        while n % p == 0:
            primes.append(p)
            n //= p
        p += 1
    if n != 1:
        primes.append(n)
    return primes

def main():
    solution = max(factorize(600851475143))
    print("solution:", solution)

if __name__ == "__main__":
    main()
