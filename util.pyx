"""Utilites for Euler problems that I find myself using a lot"""

import math

cpdef prime_factors(long long number):
    """Returns the prime factors of the input"""
    return [x for x in factors(number) if is_prime(x)]

cpdef factors(long long number):
    """Returns the factors of the input"""

    factors = []
    cdef long long candidate
    for candidate in xrange(1, int(math.sqrt(number) + 1)):
        if number % candidate == 0:
            factors.append(candidate)
            factors.append(number // candidate)
    return set(factors)

cpdef proper_divisors(long long number):
    """Returns the proper_divisors of the input"""

    factors = [1]
    cdef long long candidate
    for candidate in xrange(2, int(math.sqrt(number) + 1)):
        if number % candidate == 0:
            factors.append(candidate)
            factors.append(number // candidate)
    return set(factors)

cpdef int is_prime(long long candidate):
    """Returns true if the candidateis a prime"""

    if candidate % 2 == 0:
        return False
    cdef long long factor
    for factor in xrange(3, int(math.sqrt(candidate)) + 1, 2):
        if candidate % factor == 0:
            return False
    return True

cpdef fibonnaci(long long end):
    """Returns the fibonnaci sequence up to a max value"""

    cdef long long last = 1
    cdef long long current = 2
    cdef long long next = last + current
    sequence = [last, current]
    while next < end:
        sequence.append(next)
        next = last + current
        last = current
        current = next
    return sequence