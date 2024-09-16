"""Sequence generators."""

import math

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

def generate_fibonacci_sequence():
    """Generate the Fibonacci sequence: 1, 1, 2, 3, 5, 8, ..."""
    (f1, f2) = 0, 1
    while True:
        (f1, f2) = (f2, f1 + f2)
        yield f1
