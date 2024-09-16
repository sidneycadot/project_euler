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

english_numbers_to_words = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety"
}

def as_english_number(n: int) -> str:
    assert 0 <= n <= 1000
    s = english_numbers_to_words.get(n)
    if s is not None:
        return s
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
