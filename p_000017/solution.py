#! /usr/bin/env python3

"""
Problem 17: Number Letter Counts
================================

Link: https://projecteuler.net/problem=17

Description
===========

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def as_english_number(n: int) -> str:
    assert 0 <= n <= 1000
    if n == 0:
        return "zero"
    if n == 1:
        return "one"
    if n == 2:
        return "two"
    if n == 3:
        return "three"
    if n == 4:
        return "four"
    if n == 5:
        return "five"
    if n == 6:
        return "six"
    if n == 7:
        return "seven"
    if n == 8:
        return "eight"
    if n == 9:
        return "nine"
    if n == 10:
        return "ten"
    if n == 11:
        return "eleven"
    if n == 12:
        return "twelve"
    if n == 13:
        return "thirteen"
    if n == 14:
        return "fourteen"
    if n == 15:
        return "fifteen"
    if n == 16:
        return "sixteen"
    if n == 17:
        return "seventeen"
    if n == 18:
        return "eighteen"
    if n == 19:
        return "nineteen"
    if n == 20:
        return "twenty"
    if n == 30:
        return "thirty"
    if n == 40:
        return "forty"
    if n == 50:
        return "fifty"
    if n == 60:
        return "sixty"
    if n == 70:
        return "seventy"
    if n == 80:
        return "eighty"
    if n == 90:
        return "ninety"
    if n < 100:
        return "{}-{}".format(as_english_number(n - n % 10), as_english_number(n % 10))
    if n < 1000:
        if n % 100 == 0:
            return "{} hundred".format(as_english_number(n // 100))
        return "{} and {}".format(as_english_number(n - n % 100), as_english_number(n % 100))
    if n == 1000:
        return "one thousand"

def solve() -> int:
    return len("".join(map(as_english_number, range(1, 1001))).replace("-","").replace(" ", ""))

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
