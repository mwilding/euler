import math

def sum_of_digits_in_factorial(n):
    return sum(int(x) for x in str(math.factorial(n)))