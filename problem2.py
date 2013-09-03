"""Finds the sum of the even fibonnaci numbers less than 4000000
http://projecteuler.net/problem=2
"""

import util

def solve(end):
    """Sums the even valued fibonnaci numbers up to a max value"""
    return sum(f for f in util.fibonnaci(end) if f % 2 == 0)

