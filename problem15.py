import math

def nCr(n, r):
    f = math.factorial
    return f(n) / (f(r) * f(n - r))

def lattice_paths(width, height):
    return nCr(height * 2, width)
