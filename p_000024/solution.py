#! /usr/bin/env python3

"""
Problem 24: Lexicographic Permutations
======================================

Link: https://projecteuler.net/problem=24

Description
===========

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4.
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

import math

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

def nth_permutation(elements, n: int):
    """Return the nth permutation of the given elements."""

    sz = len(elements)

    if sz == 0:
        return ()

    period = math.factorial(sz - 1)

    head_index = (n // period) % sz
    tail_index = n % period

    head = elements[head_index]

    tail_elements = elements[:head_index] + elements[head_index + 1:]

    tail = nth_permutation(tail_elements, tail_index)

    return (head, ) + tail

def main():

    # Note: the one millionth element has index 999999.
    arrangement = nth_permutation(list(range(10)), 999999)
    solution = "".join(str(e) for e in arrangement)
    print("solution:", solution)

if __name__ == "__main__":
    main()
