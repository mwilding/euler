"""Finds the sum of all the multiples of 3 or 5 below 1000
http://projecteuler.net/problem=1
"""

def solve():
    """Finds the sum of all the multiples of 3 or 5 below 1000"""
    return sum(x for x in xrange(1, 1000) if x % 3 == 0 or x % 5 == 0)
