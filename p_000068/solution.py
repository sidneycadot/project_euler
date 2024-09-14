#! /usr/bin/env python3

"""
Problem 68: Magic 5-gon Ring
============================

Link: https://projecteuler.net/problem=68

Description
===========

Consider the following "magic" 3-gon ring, filled with the numbers 1 to 6, and each line adding to nine.

(image_1.png)

Working clockwise, and starting from the group of three with the numerically lowest external node (4,3,2 in this example),
each solution can be described uniquely. For example, the above solution can be described by the set: 4,3,2; 6,2,1; 5,1,3.

It is possible to complete the ring with four different totals: 9, 10, 11, and 12. There are eight solutions in total.

    Total    Solution Set
     9       4,2,3; 5,3,1; 6,1,2
     9       4,3,2; 6,2,1; 5,1,3
    10       2,3,5; 4,5,1; 6,1,3
    10       2,5,3; 6,3,1; 4,1,5
    11       1,4,6; 3,6,2; 5,2,4
    11       1,6,4; 5,4,2; 3,2,6
    12       1,5,6; 2,6,4; 3,4,5
    12       1,6,5; 3,5,4; 2,4,6

By concatenating each group it is possible to form 9-digit strings; the maximum string for a 3-gon ring is 432621513.

Using the numbers 1 to 10, and depending on arrangements, it is possible to form 16- and 17-digit strings.
What is the maximum 16-digit string for a "magic" 5-gon ring?

(image_2.png)
"""

import itertools

def solve() -> int:
    solutions = []
    for permutation in itertools.permutations(range(1, 1 + 10)):
        if not (permutation[0] < min(permutation[1], permutation[2], permutation[3], permutation[4])):
            continue
        spoke_1 = (permutation[0], permutation[5], permutation[6])
        spoke_2 = (permutation[1], permutation[6], permutation[7])
        spoke_3 = (permutation[2], permutation[7], permutation[8])
        spoke_4 = (permutation[3], permutation[8], permutation[9])
        spoke_5 = (permutation[4], permutation[9], permutation[5])
        if not (sum(spoke_1) == sum(spoke_2) == sum(spoke_3) == sum(spoke_4) == sum(spoke_5)):
            continue
        solution = "".join("".join(map(str, spoke)) for spoke in (spoke_1, spoke_2, spoke_3, spoke_4, spoke_5))
        if len(solution) == 16:
            solutions.append(int(solution))
    solutions.sort()
    return solutions[-1]

def main():
    solution = solve()
    print("solution:", solution)

if __name__ == "__main__":
    main()
