#! /usr/bin/env python3

"""
Problem 19: Counting Sundays
============================

Link: https://projecteuler.net/problem=19

Description
===========

You are given the following information, but you may prefer to do some research for yourself.

*   1 Jan 1900 was a Monday.
*   Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
*   A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def main():

    # Directly count off the days.

    y = 1900
    m = 1
    d = 1
    weekday = 1

    count_sundays = 0
    while y <= 2001:
        if (1901 <= y <= 2000) and (d == 1) and (weekday == 0):
            count_sundays += 1
        weekday = (weekday + 1) % 7
        if m in (1, 3, 5, 7, 8, 10, 12):
            month_days = 31
        elif m in (4, 6, 9, 11):
            month_days = 30
        else:
            leapyear = (y % 4 == 0) ^ (y % 100 == 0) ^ (y % 400 == 0)
            if leapyear:
                month_days = 29
            else:
                month_days = 28

        if d == month_days:
            d = 1
            if m == 12:
                m = 1
                y += 1
            else:
                m += 1
        else:
            d += 1

    print("solution:", count_sundays)

if __name__ == "__main__":
    main()
