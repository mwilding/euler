"""Name Scores
http://projecteuler.net/problem=22
"""

import csv

def sum_name_scores(path):
    """Reads the file at path, and returns the sum of the namescores"""

    with open(path, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        names = reader.next()
        names.sort()
    
    total = 0
    for i in xrange(len(names)):
        total += (i + 1) * sum(ord(c) - 64 for c in names[i])
    return total
