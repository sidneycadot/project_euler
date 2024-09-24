#! /usr/bin/env python3

"""Solve all Project Euler problems."""

import time
import importlib
import contextlib
from typing import NamedTuple, Optional
from enum import Flag

from colorama import Fore, Style

class P(Flag):
    UNKNOWN = 1
    OPTIMAL = 2
    SLOW    = 4
    UGLY    = 8

class ProblemDescription(NamedTuple):
    index: int
    title: str
    difficulty: Optional[int]
    solution: Optional[int]
    flags: P

# These are known-good solutions.
known_solutions: dict[int, ProblemDescription] = {
     1 : ProblemDescription(    1, "Multiples of 3 or 5"                      ,  5 ,           233168 , P.OPTIMAL),
     2 : ProblemDescription(    2, "Even Fibonacci Numbers"                   ,  5 ,          4613732 , P.OPTIMAL),
     3 : ProblemDescription(    3, "Largest Prime Factor"                     ,  5 ,             6857 , P.OPTIMAL),
     4 : ProblemDescription(    4, "Largest Palindrome Product"               ,  5 ,           906609 , P.OPTIMAL),
     5 : ProblemDescription(    5, "Smallest Multiple"                        ,  5 ,        232792560 , P.OPTIMAL),
     6 : ProblemDescription(    6, "Sum Square Difference"                    ,  5 ,         25164150 , P.OPTIMAL),
     7 : ProblemDescription(    7, "10001st Prime"                            ,  5 ,           104743 , P.UNKNOWN),
     8 : ProblemDescription(    8, "Largest Product in a Series"              ,  5 ,      23514624000 , P.UNKNOWN),
     9 : ProblemDescription(    9, "Special Pythagorean Triplet"              ,  5 ,         31875000 , P.UNKNOWN),
    10 : ProblemDescription(   10, "Summation of Primes"                      ,  5 ,     142913828922 , P.OPTIMAL),
    11 : ProblemDescription(   11, "Largest Product in a Grid"                ,  5 ,         70600674 , P.OPTIMAL),
    12 : ProblemDescription(   12, "Highly Divisible Triangular Number"       ,  5 ,         76576500 , P.OPTIMAL),
    13 : ProblemDescription(   13, "Large Sum"                                ,  5 ,       5537376230 , P.OPTIMAL),
    14 : ProblemDescription(   14, "Longest Collatz Sequence"                 ,  5 ,           837799 , P.OPTIMAL),
    15 : ProblemDescription(   15, "Lattice Paths"                            ,  5 ,     137846528820 , P.OPTIMAL),
    16 : ProblemDescription(   16, "Power Digit Sum"                          ,  5 ,             1366 , P.OPTIMAL),
    17 : ProblemDescription(   17, "Number Letter Counts"                     ,  5 ,            21124 , P.OPTIMAL),
    18 : ProblemDescription(   18, "Maximum Path Sum I"                       ,  5 ,             1074 , P.UNKNOWN),
    19 : ProblemDescription(   19, "Counting Sundays"                         ,  5 ,              171 , P.UNKNOWN),
    20 : ProblemDescription(   20, "Factorial Digit Sum"                      ,  5 ,              648 , P.OPTIMAL),
    21 : ProblemDescription(   21, "Amicable Numbers"                         ,  5 ,            31626 , P.UNKNOWN),
    22 : ProblemDescription(   22, "Names Scores"                             ,  5 ,        871198282 , P.OPTIMAL),
    23 : ProblemDescription(   23, "Non-Abundant Sums"                        ,  5 ,          4179871 , P.UNKNOWN), # Quite slow (30s)
    24 : ProblemDescription(   24, "Lexicographic Permutations"               ,  5 ,       2783915460 , P.UNKNOWN),
    25 : ProblemDescription(   25, "1000-digit Fibonacci Number"              ,  5 ,             4782 , P.OPTIMAL),
    26 : ProblemDescription(   26, "Reciprocal Cycles"                        ,  5 ,              983 , P.UNKNOWN),
    27 : ProblemDescription(   27, "Quadratic Primes"                         ,  5 ,           -59231 , P.UNKNOWN),
    28 : ProblemDescription(   28, "Number Spiral Diagonals"                  ,  5 ,        669171001 , P.OPTIMAL),
    29 : ProblemDescription(   29, "Distinct Powers"                          ,  5 ,             9183 , P.OPTIMAL),
    30 : ProblemDescription(   30, "Digit Fifth Powers"                       ,  5 ,           443839 , P.UNKNOWN),
    31 : ProblemDescription(   31, "Coin Sums"                                ,  5 ,            73682 , P.UNKNOWN),
    32 : ProblemDescription(   32, "Pandigital Products"                      ,  5 ,            45228 , P.UNKNOWN),
    33 : ProblemDescription(   33, "Digit Cancelling Fractions"               ,  5 ,              100 , P.UNKNOWN),
    34 : ProblemDescription(   34, "Digit Factorials"                         ,  5 ,            40730 , P.UNKNOWN),
    35 : ProblemDescription(   35, "Circular Primes"                          ,  5 ,               55 , P.UNKNOWN),
    36 : ProblemDescription(   36, "Double-base Palindromes"                  ,  5 ,           872187 , P.UNKNOWN),
    37 : ProblemDescription(   37, "Truncatable Primes"                       ,  5 ,           748317 , P.UNKNOWN),
    38 : ProblemDescription(   38, "Pandigital Multiples"                     ,  5 ,        932718654 , P.UNKNOWN),
    39 : ProblemDescription(   39, "Integer Right Triangles"                  ,  5 ,              840 , P.UNKNOWN),
    40 : ProblemDescription(   40, "Champernowne's Constant"                  ,  5 ,              210 , P.UNKNOWN),
    41 : ProblemDescription(   41, "Pandigital Prime"                         ,  5 ,          7652413 , P.UNKNOWN),
    42 : ProblemDescription(   42, "Coded Triangle Numbers"                   ,  5 ,              162 , P.UNKNOWN),
    43 : ProblemDescription(   43, "Sub-string Divisibility"                  ,  5 ,      16695334890 , P.UNKNOWN),
    44 : ProblemDescription(   44, "Pentagon Numbers"                         ,  5 ,          5482660 , P.SLOW   ),  # Very slow (~ 15 minutes).
    45 : ProblemDescription(   45, "Triangular, Pentagonal, and Hexagonal"    ,  5 ,       1533776805 , P.UNKNOWN),
    46 : ProblemDescription(   46, "Goldbach's Other Conjecture"              ,  5 ,             5777 , P.UNKNOWN),
    47 : ProblemDescription(   47, "Distinct Primes Factors"                  ,  5 ,           134043 , P.UNKNOWN),
    48 : ProblemDescription(   48, "Self Powers"                              ,  5 ,       9110846700 , P.UNKNOWN),
    49 : ProblemDescription(   49, "Prime Permutations"                       ,  5 ,     296962999629 , P.UNKNOWN),
    50 : ProblemDescription(   50, "Consecutive Prime Sum"                    ,  5 ,           997651 , P.UNKNOWN),
    51 : ProblemDescription(   51, "Prime Digit Replacements"                 , 15 ,             None , P.UNKNOWN),
    52 : ProblemDescription(   52, "Permuted Multiples"                       ,  5 ,           142857 , P.UNKNOWN),
    53 : ProblemDescription(   53, "Combinatoric Selections"                  ,  5 ,             4075 , P.UNKNOWN),
    54 : ProblemDescription(   54, "Poker Hands"                              , 10 ,             None , P.UNKNOWN),
    55 : ProblemDescription(   55, "Lychrel Numbers"                          ,  5 ,             None , P.UNKNOWN),
    56 : ProblemDescription(   56, "Powerful Digit Sum"                       ,  5 ,              972 , P.UNKNOWN),
    57 : ProblemDescription(   57, "Square Root Convergents"                  ,  5 ,             None , P.UNKNOWN),
    58 : ProblemDescription(   58, "Spiral Primes"                            ,  5 ,             None , P.UNKNOWN),
    59 : ProblemDescription(   59, "XOR Decryption"                           ,  5 ,           129448 , P.UNKNOWN),
    60 : ProblemDescription(   60, "Prime Pair Sets"                          , 20 ,             None , P.UNKNOWN),
    61 : ProblemDescription(   61, "Cyclical Figurate Numbers"                , 20 ,            28684 , P.UNKNOWN),
    62 : ProblemDescription(   62, "Cubic Permutations"                       , 15 ,             None , P.UNKNOWN),
    63 : ProblemDescription(   63, "Powerful Digit Counts"                    ,  5 ,             None , P.UNKNOWN),
    64 : ProblemDescription(   64, "Odd Period Square Roots"                  , 20 ,             None , P.UNKNOWN),
    65 : ProblemDescription(   65, "Convergents of e"                         , 15 ,              272 , P.UNKNOWN),
    66 : ProblemDescription(   66, "Diophantine Equation"                     , 25 ,             None , P.UNKNOWN),
    67 : ProblemDescription(   67, "Maximum Path Sum II"                      ,  5 ,             7273 , P.UNKNOWN),
    68 : ProblemDescription(   68, "Magic 5-gon Ring"                         , 25 , 6531031914842725 , P.UNKNOWN),
    69 : ProblemDescription(   69, "Totient Maximum"                          , 10 ,           510510 , P.UNKNOWN),
    70 : ProblemDescription(   70, "Totient Permutation"                      , 20 ,          8319823 , P.SLOW   ),
    71 : ProblemDescription(   71, "Ordered Fractions"                        , 10 ,             None , P.UNKNOWN),
    72 : ProblemDescription(   72, "Counting Fractions"                       , 20 ,     303963552391 , P.UNKNOWN),
    73 : ProblemDescription(   73, "Counting Fractions in a Range"            , 15 ,             None , P.UNKNOWN),
    74 : ProblemDescription(   74, "Digit Factorial Chains"                   , 15 ,             None , P.UNKNOWN),
    75 : ProblemDescription(   75, "Singular Integer Right Triangles"         , 25 ,             None , P.UNKNOWN),
    76 : ProblemDescription(   76, "Counting Summations"                      , 10 ,        190569291 , P.UNKNOWN),
    77 : ProblemDescription(   77, "Prime Summations"                         , 25 ,             None , P.UNKNOWN),
    78 : ProblemDescription(   78, "Coin Partitions"                          , 30 ,             None , P.UNKNOWN),
    79 : ProblemDescription(   79, "Passcode Derivation"                      ,  5 ,         73162890 , P.UNKNOWN),
    80 : ProblemDescription(   80, "Square Root Digital Expansion"            , 20 ,            40886 , P.UNKNOWN),
    81 : ProblemDescription(   81, "Path Sum: Two Ways"                       , 10 ,             None , P.UNKNOWN),
    82 : ProblemDescription(   82, "Path Sum: Three Ways"                     , 20 ,             None , P.UNKNOWN),
    83 : ProblemDescription(   83, "Path Sum: Four Ways"                      , 25 ,             None , P.UNKNOWN),
    84 : ProblemDescription(   84, "Monopoly Odds"                            , 35 ,             None , P.UNKNOWN),
    85 : ProblemDescription(   85, "Counting Rectangles"                      , 15 ,             2772 , P.UNKNOWN),
    86 : ProblemDescription(   86, "Cuboid Route"                             , 35 ,             None , P.UNKNOWN),
    87 : ProblemDescription(   87, "Prime Power Triples"                      , 20 ,          1097343 , P.SLOW   ),  # Very slow (~ 41 minutes)
    88 : ProblemDescription(   88, "Product-sum Numbers"                      , 40 ,             None , P.UNKNOWN),
    89 : ProblemDescription(   89, "Roman Numerals"                           , 20 ,             None , P.UNKNOWN),
    90 : ProblemDescription(   90, "Cube Digit Pairs"                         , 40 ,             None , P.UNKNOWN),
    91 : ProblemDescription(   91, "Right Triangles with Integer Coordinates" , 25 ,             None , P.UNKNOWN),
    92 : ProblemDescription(   92, "Square Digit Chains"                      ,  5 ,          8581146 , P.UNKNOWN),
    93 : ProblemDescription(   93, "Arithmetic Expressions"                   , 35 ,             None , P.UNKNOWN),
    94 : ProblemDescription(   94, "Almost Equilateral Triangles"             , 35 ,             None , P.UNKNOWN),
    95 : ProblemDescription(   95, "Amicable Chains"                          , 30 ,             None , P.UNKNOWN),
    96 : ProblemDescription(   96, "Su Doku"                                  , 25 ,             None , P.UNKNOWN),
    97 : ProblemDescription(   97, "Large Non-Mersenne Prime"                 ,  5 ,       8739992577 , P.UNKNOWN),
    98 : ProblemDescription(   98, "Anagramic Squares"                        , 35 ,             None , P.UNKNOWN),
    99 : ProblemDescription(   99, "Largest Exponential"                      , 10 ,              709 , P.UNKNOWN),
   100 : ProblemDescription(  100, "Arranged Probability"                     , 30 ,             None , P.UNKNOWN)
}

def check_module_docstring(problem: ProblemDescription, module_docstring: str) -> None:
    title_line = f"Problem {problem.index}: {problem.title}"
    docstring_preamble_lines = [
        "",
        title_line,
        "=" * len(title_line),
        "",
        f"Link: https://projecteuler.net/problem={problem.index}",
        "",
        "Description",
        "===========",
        ""
    ]
    docstring_preamble = "".join(line + "\n" for line in docstring_preamble_lines)

    if not module_docstring.startswith(docstring_preamble):
        print(repr(docstring_preamble))
        print(repr(module_docstring[:len(docstring_preamble)]))
        raise RuntimeError(f"Bad docstring in solution of problem {problem.index}.")

def main():

    for (problem_index, problem) in known_solutions.items():

        assert problem_index == problem.index

        if not (34 <= problem.index <= 34):
            continue

        directory = f"p_{problem.index:06d}"
        module_name = f"{directory}.solution"

        try:
            module = importlib.import_module(module_name)
        except ModuleNotFoundError:
            module = None

        if module is None:
            result = f"{Fore.LIGHTYELLOW_EX}UNABLE TO IMPORT MODULE{Style.RESET_ALL}"
        else:
            if getattr(module, "__doc__") is None:
                raise RuntimeError(f"Implementation of problem {problem.index} doesn't have a docstring.")
            check_module_docstring(problem, module.__doc__)

            try:
                with contextlib.chdir(directory):
                    t1 = time.monotonic()
                    solution = module.solve()
                    t2 = time.monotonic()
                    duration = t2 - t1
            except AttributeError:
                solution = None
                duration = 0.0

            if solution is None:
                result = f"{Fore.LIGHTYELLOW_EX}UNABLE TO RUN{Style.RESET_ALL}"
            elif solution == problem.solution:
                result = f"{Fore.LIGHTGREEN_EX}{solution}{Style.RESET_ALL}"
            else:
                result = f"{Fore.LIGHTRED_EX}{solution}{Style.RESET_ALL} (expected {problem.solution})"

        print(f"{problem.index:3d} | {Fore.LIGHTCYAN_EX}{problem.title:37s}{Style.RESET_ALL} | {Fore.LIGHTCYAN_EX}{problem.difficulty:3d}{Style.RESET_ALL} | wallclock time: {duration:9.4f}s | result: {result:s}")

if __name__ == "__main__":
    main()
