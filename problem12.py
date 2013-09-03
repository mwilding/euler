import math
import util

def first_triagle_with_divisors(n):
    triangle_number = 1; i = 1 
    while len(util.factors(triangle_number)) <= n:
        i += 1
        triangle_number += i
    return triangle_number
