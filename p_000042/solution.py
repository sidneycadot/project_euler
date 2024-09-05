#! /usr/bin/env python3

"""
Problem 42: Coded Triangle Numbers
==================================

Link: https://projecteuler.net/problem=42

Description
===========

The nth term of the sequence of triangle numbers is given by, t[n] == ½n(n+1); so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words,
how many are triangle words?
"""

from pelib import is_triangle_number

def unquote(s: str) -> str:
    assert s.startswith('"')
    assert s.endswith('"')
    return s[1:-1]

def word_value(s: str) -> int:
    return sum(ord(c) - ord('A') + 1 for c in s)

def solve() -> int:

    with open("words.txt", "r") as fi:
        words = list(map(unquote, fi.readline().split(",")))

    triangle_words = [word for word in words if is_triangle_number(word_value(word))]

    return len(triangle_words)

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
