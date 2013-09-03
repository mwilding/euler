from util import *

def nth_prime(n):
    found = 1
    candidate = 1
    while found != n:
        candidate += 2 # Start at 3
        if is_prime(candidate):
            found += 1
    return candidate
