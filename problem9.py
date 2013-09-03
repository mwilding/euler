def pythagorean_triplet(n):
    for c in xrange(3, n + 1):
        for b in xrange(2, c):
            for a in xrange(1, b):
                if a**2 + b**2 == c**2 and a + b + c == n:
                    return a * b * c