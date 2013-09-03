"""Find the largest prime factor of 600851475143
http://projecteuler.net/problem=3
"""

import util

def largest_prime_factor(n):
    return max(util.prime_factors(n))