#! /usr/bin/env python3

"""
Problem 22: Names Scores
========================

Link: https://projecteuler.net/problem=22

Description
===========

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position
in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53 is the 938th name in the list.
So, COLIN would obtain a score of 938×53 = 49714.

What is the total of all the name scores in the file?
"""

def unquote(s: str) -> str:
    assert s.startswith('"')
    assert s.endswith('"')
    return s[1:-1]

def name_score(s: str) -> int:
    return sum(ord(c) - ord('A') + 1 for c in s)

def solve() -> int:
    with open("names.txt", "r") as fi:
        names = list(map(unquote, fi.readline().split(",")))
    names.sort()
    return sum(idx * name_score(name) for (idx, name) in enumerate(names, 1))

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
