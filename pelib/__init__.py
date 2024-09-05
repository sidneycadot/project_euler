"""Often-used functions in the Project Euler solution programs."""

import functools
import operator
import math
from collections.abc import Iterable

def is_prime(n: int) -> bool:
    """Check if the given number is a prime, by trial division."""

    if n < 2:
        return False

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

is_prime_cached = functools.cache(is_prime)

def next_prime(n: int) -> int:
    """Return the smallest prime greater than n."""
    if n < 2:
        return 2

    n += 1
    while not is_prime(n):
        n += 1

    return n

def prime_sieve(n: int) -> list[int]:
    """Generate a list of all prime numbers up to (but not including) n."""
    if n < 0:
        raise ValueError("Argument n must be non-negative.")
    primes = []
    arr = bytearray(n)
    for p in range(2, n):
        if arr[p] == 0:
            primes.append(p)
            k = p * p
            while k < n:
                arr[k] = 1
                k += p
    return primes

def factorize(n: int) -> list[tuple[int, int]]:
    """Returns the factorization of the argument as a list of (prime, exponent) pairs."""
    if n < 1:
        raise ValueError("Argument n must be positive.")
    factors = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            e += 1
            n //= p
        if e != 0:
            factors.append((p, e))
        p += 1
    if n != 1:
        factors.append((n, 1))
    return factors

def divisors(n: int) -> list[int]:
    """Return the proper divisors of n (i.e., the positive divisors less than n)."""
    return [d for d in range(1, n) if n % d == 0]

def product(iterable: Iterable[int]) -> int:
    """Return the product of integers,"""
    return functools.reduce(operator.mul, iterable, 1)

def powermod(a: int, b: int, modulo: int) -> int:
    r = 1
    while b != 0:
        if b % 2 != 0:
            r = (r * a) % modulo
        a = (a * a) % modulo
        b //= 2
    return r

def generate_triangle_numbers():
    n = 1
    p = 0
    while True:
        p += n
        n += 1
        yield p

def is_triangle_number(n: int) -> bool:
    k = round(0.5 * (math.sqrt(1 + 8 * n) - 1.0))
    return k * (k + 1) // 2 == n

def generate_pentagonal_numbers():
    n = 1
    p = 0
    while True:
        p += n
        n += 3
        yield p

def pentagonal_index(pentagonal : int) -> int:
    return round((1.0 + math.sqrt(1 + 24 * pentagonal)) / 6.0)

def pentagonal_from_index(index : int) -> int:
    return (index * (3 * index - 1)) // 2

def is_pentagonal_number(maybe_pentagonal: int) -> bool:
    pentagonal = pentagonal_from_index(pentagonal_index(maybe_pentagonal))
    return maybe_pentagonal == pentagonal

def generate_hexagonal_numbers():
    n = 1
    p = 0
    while True:
        p += n
        n += 4
        yield p

def digit_sum(n: int, base: int=10) -> int:
    """Return the sum of the digits in n."""
    s = 0
    while n != 0:
        s += (n % base)
        n //= base
    return s
