#! /usr/bin/env python3

"""Solve all Project Euler problems."""

import time
import importlib
import contextlib
from typing import NamedTuple, Optional

from colorama import Fore, Style

class ProblemDescription(NamedTuple):
    index: int
    title: str
    difficulty: Optional[int]
    solution: Optional[int]

# These are known-good solutions.
known_solutions: dict[int, ProblemDescription] = {
     1 : ProblemDescription(    1, "Multiples of 3 or 5"                      ,  5 ,           233168 ),
     2 : ProblemDescription(    2, "Even Fibonacci Numbers"                   ,  5 ,          4613732 ),
     3 : ProblemDescription(    3, "Largest Prime Factor"                     ,  5 ,             6857 ),
     4 : ProblemDescription(    4, "Largest Palindrome Product"               ,  5 ,           906609 ),
     5 : ProblemDescription(    5, "Smallest Multiple"                        ,  5 ,        232792560 ),
     6 : ProblemDescription(    6, "Sum Square Difference"                    ,  5 ,         25164150 ),
     7 : ProblemDescription(    7, "10001st Prime"                            ,  5 ,           104743 ),
     8 : ProblemDescription(    8, "Largest Product in a Series"              ,  5 ,      23514624000 ),
     9 : ProblemDescription(    9, "Special Pythagorean Triplet"              ,  5 ,         31875000 ),
    10 : ProblemDescription(   10, "Summation of Primes"                      ,  5 ,     142913828922 ),
    11 : ProblemDescription(   11, "Largest Product in a Grid"                ,  5 ,         70600674 ),
    12 : ProblemDescription(   12, "Highly Divisible Triangular Number"       ,  5 ,         76576500 ),
    13 : ProblemDescription(   13, "Large Sum"                                ,  5 ,       5537376230 ),
    14 : ProblemDescription(   14, "Longest Collatz Sequence"                 ,  5 ,           837799 ),
    15 : ProblemDescription(   15, "Lattice Paths"                            ,  5 ,     137846528820 ),
    16 : ProblemDescription(   16, "Power Digit Sum"                          ,  5 ,             1366 ),
    17 : ProblemDescription(   17, "Number Letter Counts"                     ,  5 ,            21124 ),
    18 : ProblemDescription(   18, "Maximum Path Sum I"                       ,  5 ,             1074 ),
    19 : ProblemDescription(   19, "Counting Sundays"                         ,  5 ,              171 ),
    20 : ProblemDescription(   20, "Factorial Digit Sum"                      ,  5 ,              648 ),
    21 : ProblemDescription(   21, "Amicable Numbers"                         ,  5 ,            31626 ),
    22 : ProblemDescription(   22, "Names Scores"                             ,  5 ,        871198282 ),
    23 : ProblemDescription(   23, "Non-Abundant Sums"                        ,  5 ,          4179871 ),
    24 : ProblemDescription(   24, "Lexicographic Permutations"               ,  5 ,       2783915460 ),
    25 : ProblemDescription(   25, "1000-digit Fibonacci Number"              ,  5 ,             4782 ),
    26 : ProblemDescription(   26, "Reciprocal Cycles"                        ,  5 ,              983 ),
    27 : ProblemDescription(   27, "Quadratic Primes"                         ,  5 ,           -59231 ),
    28 : ProblemDescription(   28, "Number Spiral Diagonals"                  ,  5 ,        669171001 ),
    29 : ProblemDescription(   29, "Distinct Powers"                          ,  5 ,             9183 ),
    30 : ProblemDescription(   30, "Digit Fifth Powers"                       ,  5 ,           443839 ),
    31 : ProblemDescription(   31, "Coin Sums"                                ,  5 ,            73682 ),
    32 : ProblemDescription(   32, "Pandigital Products"                      ,  5 ,            45228 ),
    33 : ProblemDescription(   33, "Digit Cancelling Fractions"               ,  5 ,              100 ),
    34 : ProblemDescription(   34, "Digit Factorials"                         ,  5 ,            40730 ),
    35 : ProblemDescription(   35, "Circular Primes"                          ,  5 ,               55 ),
    36 : ProblemDescription(   36, "Double-base Palindromes"                  ,  5 ,           872187 ),
    37 : ProblemDescription(   37, "Truncatable Primes"                       ,  5 ,           748317 ),
    38 : ProblemDescription(   38, "Pandigital Multiples"                     ,  5 ,        932718654 ),
    39 : ProblemDescription(   39, "Integer Right Triangles"                  ,  5 ,              840 ),
    40 : ProblemDescription(   40, "Champernowne's Constant"                  ,  5 ,              210 ),
    41 : ProblemDescription(   41, "Pandigital Prime"                         ,  5 ,          7652413 ),
    42 : ProblemDescription(   42, "Coded Triangle Numbers"                   ,  5 ,              162 ),
    43 : ProblemDescription(   43, "Sub-string Divisibility"                  ,  5 ,      16695334890 ),
    44 : ProblemDescription(   44, "Pentagon Numbers"                         ,  5 ,          5482660 ),  # VERY SLOW (15 minutes).
    45 : ProblemDescription(   45, "Triangular, Pentagonal, and Hexagonal"    ,  5 ,       1533776805 ),
    46 : ProblemDescription(   46, "Goldbach's Other Conjecture"              ,  5 ,             5777 ),
    47 : ProblemDescription(   47, "Distinct Primes Factors"                  ,  5 ,           134043 ),
    48 : ProblemDescription(   48, "Self Powers"                              ,  5 ,       9110846700 ),
    49 : ProblemDescription(   49, "Prime Permutations"                       ,  5 ,     296962999629 ),
    50 : ProblemDescription(   50, "Consecutive Prime Sum"                    ,  5 ,           997651 ),
    51 : ProblemDescription(   51, "Prime Digit Replacements"                 , 15 ,             None ),
    52 : ProblemDescription(   52, "Permuted Multiples"                       ,  5 ,           142857 ),
    53 : ProblemDescription(   53, "Combinatoric Selections"                  ,  5 ,             4075 ),
    54 : ProblemDescription(   54, "Poker Hands"                              , 10 ,             None ),
    55 : ProblemDescription(   55, "Lychrel Numbers"                          ,  5 ,             None ),
    56 : ProblemDescription(   56, "Powerful Digit Sum"                       ,  5 ,              972 ),
    57 : ProblemDescription(   57, "Square Root Convergents"                  ,  5 ,             None ),
    58 : ProblemDescription(   58, "Spiral Primes"                            ,  5 ,             None ),
    59 : ProblemDescription(   59, "XOR Decryption"                           ,  5 ,           129448 ),
    60 : ProblemDescription(   60, "Prime Pair Sets"                          , 20 ,             None ),
    61 : ProblemDescription(   61, "Cyclical Figurate Numbers"                , 20 ,            28684 ),
    62 : ProblemDescription(   62, "Cubic Permutations"                       , 15 ,             None ),
    63 : ProblemDescription(   63, "Powerful Digit Counts"                    ,  5 ,             None ),
    64 : ProblemDescription(   64, "Odd Period Square Roots"                  , 20 ,             None ),
    65 : ProblemDescription(   65, "Convergents of e"                         , 15 ,             None ),
    66 : ProblemDescription(   66, "Diophantine Equation"                     , 25 ,             None ),
    67 : ProblemDescription(   67, "Maximum Path Sum II"                      ,  5 ,             7273 ),
    68 : ProblemDescription(   68, "Magic 5-gon Ring"                         , 25 , 6531031914842725 ),
    69 : ProblemDescription(   69, "Totient Maximum"                          , 10 ,           510510 ),
    70 : ProblemDescription(   70, "Totient Permutation"                      , 20 ,             None ),
    71 : ProblemDescription(   71, "Ordered Fractions"                        , 10 ,             None ),
    72 : ProblemDescription(   72, "Counting Fractions"                       , 20 ,             None ),
    73 : ProblemDescription(   73, "Counting Fractions in a Range"            , 15 ,             None ),
    74 : ProblemDescription(   74, "Digit Factorial Chains"                   , 15 ,             None ),
    75 : ProblemDescription(   75, "Singular Integer Right Triangles"         , 25 ,             None ),
    76 : ProblemDescription(   76, "Counting Summations"                      , 10 ,        190569291 ),
    77 : ProblemDescription(   77, "Prime Summations"                         , 25 ,             None ),
    78 : ProblemDescription(   78, "Coin Partitions"                          , 30 ,             None ),
    79 : ProblemDescription(   79, "Passcode Derivation"                      ,  5 ,             None ),
    80 : ProblemDescription(   80, "Square Root Digital Expansion"            , 20 ,             None ),
    81 : ProblemDescription(   81, "Path Sum: Two Ways"                       , 10 ,             None ),
    82 : ProblemDescription(   82, "Path Sum: Three Ways"                     , 20 ,             None ),
    83 : ProblemDescription(   83, "Path Sum: Four Ways"                      , 25 ,             None ),
    84 : ProblemDescription(   84, "Monopoly Odds"                            , 35 ,             None ),
    85 : ProblemDescription(   85, "Counting Rectangles"                      , 15 ,             2772 ),
    86 : ProblemDescription(   86, "Cuboid Route"                             , 35 ,             None ),
    87 : ProblemDescription(   87, "Prime Power Triples"                      , 20 ,          1097343 ),  # VERY SLOW
    88 : ProblemDescription(   88, "Product-sum Numbers"                      , 40 ,             None ),
    89 : ProblemDescription(   89, "Roman Numerals"                           , 20 ,             None ),
    90 : ProblemDescription(   90, "Cube Digit Pairs"                         , 40 ,             None ),
    91 : ProblemDescription(   91, "Right Triangles with Integer Coordinates" , 25 ,             None ),
    92 : ProblemDescription(   92, "Square Digit Chains"                      ,  5 ,          8581146 ),
    93 : ProblemDescription(   93, "Arithmetic Expressions"                   , 35 ,             None ),
    94 : ProblemDescription(   94, "Almost Equilateral Triangles"             , 35 ,             None ),
    95 : ProblemDescription(   95, "Amicable Chains"                          , 30 ,             None ),
    96 : ProblemDescription(   96, "Su Doku"                                  , 25 ,             None ),
    97 : ProblemDescription(   97, "Large Non-Mersenne Prime"                 ,  5 ,       8739992577 ),
    98 : ProblemDescription(   98, "Anagramic Squares"                        , 35 ,             None ),
    99 : ProblemDescription(   99, "Largest Exponential"                      , 10 ,              709 ),
   100 : ProblemDescription(  100, "Arranged Probability"                     , 30 ,              None)
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

        if not (51 <= problem.index <= 100):
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

        print(f"{problem.index:3d} | {Fore.LIGHTCYAN_EX}{problem.title:37s}{Style.RESET_ALL} | wallclock time: {duration:8.4f}s | result: {result:s}")

if __name__ == "__main__":
    main()
