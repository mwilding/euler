import util

def sum_of_primes_below(n):
    sum = 2
    for candidate in xrange(3, n + 1, 2):
        if util.is_prime(candidate):
            sum += candidate
    return sum