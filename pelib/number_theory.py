"""Number-theoretical functions."""

import math
import functools

from .miscellaneous import product

def is_prime(n: int) -> bool:
    """Check if the given number is a prime.

    This implementation uses trial division, making it very slow for big numbers.
    """

    if n < 2:
        return False

    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True

# A cached version of the 'is_prime' routine.
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

def powermod(a: int, b: int, modulo: int) -> int:
    """Return (a**b) mod (modulo)."""
    r = 1
    while b != 0:
        if b % 2 != 0:
            r = (r * a) % modulo
        a = (a * a) % modulo
        b //= 2
    return r

def gcd(*integers) -> int:
    """Return the greatest common divisor of the integer arguments."""
    return math.gcd(*integers)

def lcm(*integers) -> int:
    """Return the least common multiple of the integer arguments."""
    return math.lcm(*integers)

def euler_phi(n: int) -> int:
    """Return the number of positive integers < n that are relative prime to n."""
    if n == 0:
        return 0
    return product(p ** (e - 1) * (p - 1) for (p, e) in factorize(abs(n)))
