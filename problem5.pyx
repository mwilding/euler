import operator

cpdef long long smallest_multiple_of_series(int max_factor):
    
    factors_that_matter = range(max_factor, max_factor / 2, -1) 
    other_factors = factors_that_matter[1:]

    cdef long long max_product = reduce(operator.mul, factors_that_matter)
    cdef long long largest_factor = factors_that_matter[0]
    cdef long long largest_product = largest_factor
    cdef long long little_factor = 0
    while largest_product < max_product:
        all_divide = True
        for little_factor in other_factors:
            if largest_product % little_factor != 0:
                all_divide = False
                break
        if all_divide:
            return largest_product
        largest_product += largest_factor
