#! /usr/bin/env python3

"""Solve all Project Euler problems."""

import time
import importlib
import contextlib
from colorama import Fore, Style

# These are known-good solutions.
known_solutions: dict[int, int] = {
    1   : 233168,
    2   : 4613732,
    3   : 6857,
    4   : 906609,
    5   : 232792560,
    6   : 25164150,
    7   : 104743,
    8   : 23514624000,
    9   : 31875000,
    10  : 142913828922,
    11  : 70600674,
    12  : 76576500,
    13  : 5537376230,
    14  : 837799,
    15  : 137846528820,
    16  : 1366,
    17  : 21124,
    18  : 1074,
    19  : 171,
    20  : 648,
    21  : 31626,
    22  : 871198282,
    23  : 4179871,
    24  : 2783915460,
    25  : 4782,
    26  : 983,
    27  : -59231,
    28  : 669171001,
    29  : 9183,
    30  : 443839,
    31  : 73682,
    32  : 45228,
    33  : 100,
    34  : 40730,
    35  : 55,
    36  : 872187,
    37  : 748317,
    38  : 932718654,
    39  : 840,
    40  : 210,
    41  : 7652413,
    42  : 162,
    43  : 16695334890,
    44  : 5482660,
    45  : 1533776805,
    46  : 5777,
    47  : 134043,
    48  : 9110846700,
    49  : 296962999629,
    50  : 997651
}

def main():
    for (problem_nr, correct_solution) in known_solutions.items():
        if problem_nr <= 0:
            continue
        directory = f"p_{problem_nr:06d}"
        module_name = f"{directory}.solution"
        module = importlib.import_module(module_name)
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
            result =Fore.LIGHTYELLOW_EX + "UNABLE TO RUN" + Style.RESET_ALL
        elif solution == correct_solution:
            result = Fore.LIGHTGREEN_EX + str(solution) + Style.RESET_ALL
        else:
            result = Fore.LIGHTRED_EX + str(solution) + Style.RESET_ALL + " (expected {})".format(correct_solution)

        print("{} | wallclock time: {:8.4f}s | result: {}".format(module_name, duration, result))

if __name__ == "__main__":
    main()
