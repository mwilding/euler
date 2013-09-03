def go():
    sum_of_squares = sum(x**2 for x in xrange(101))
    square_of_sum = sum(x for x in xrange(101))**2
    return square_of_sum - sum_of_squares
    