#! /usr/bin/env python3

"""
The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is,

   (1 + 2 + ... + 10)^2 = 55^2 = 3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is

    3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def main():
    numbers = list(range(1, 101))
    sum_of_squares = sum(k**2 for k in numbers)
    square_of_sum = sum(numbers) ** 2
    solution = square_of_sum - sum_of_squares
    print("solution:", solution)


if __name__ == "__main__":
    main()
