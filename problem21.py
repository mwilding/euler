import util
import math

def factors(number):
    """Returns the factors of the input"""

    factors = []
    for candidate in xrange(1, int(math.sqrt(number) + 1)):
        if number % candidate == 0:
            factors.append(candidate)
            factors.append(number // candidate)
    return set(factors)

_hash = {}
def sum_of_proper_divisors(number):
    """Returns the sum of proper divisors of n, optimized with hash"""
    hash_hit = _hash.get(number)
    if hash_hit:
        return hash_hit
    computed_sum = sum(util.proper_divisors(number))
    _hash[number] = computed_sum
    return computed_sum

def sum_amicable_numbers_below(max_range):
    """Returns the sum of amicable numbers below n"""

    amicable_numbers = set()
    for this_number in xrange(1, max_range):
        other_number = sum_of_proper_divisors(this_number)
        if this_number == other_number:
            continue
        if sum_of_proper_divisors(other_number) == this_number:
            amicable_numbers.add(this_number)
            amicable_numbers.add(other_number)
    return sum(amicable_numbers)

