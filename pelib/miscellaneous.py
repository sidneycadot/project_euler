"""Miscellaneous functions."""

import math
import functools
import operator
from collections.abc import Iterable

def product(iterable: Iterable[int]) -> int:
    """Return the product of integers,"""
    return functools.reduce(operator.mul, iterable, 1)

def digit_sum(n: int, base: int=10) -> int:
    """Return the sum of the digits in n."""
    s = 0
    while n != 0:
        s += (n % base)
        n //= base
    return s

def factorial(n: int) -> int:
    return math.factorial(n)

def binomial(n: int, k: int) -> int:
    assert 0 <= k <= n
    return math.comb(n, k)

def generate_lexicographical_order(elements):
    """Generate all permutations of distinct objects.

    If the elements are sorted, the elements will be yielded in lexicographical order.

    This is equivalent to the itertools.permutations() iterator.
    """
    if len(elements) == 0:
        yield ()
    else:
        for (i, head) in enumerate(elements):
            tail_elements = elements[:i] + elements[i + 1:]
            yield from ((head, ) + tail for tail in generate_lexicographical_order(tail_elements))
