def is_pallindrome(phrase):
    return phrase == phrase[::-1]

def largest_pallindrome_product(n_digits):

    biggest = 0
    max_candidate = 10**n_digits - 1
    for x in xrange(max_candidate, 0, -1):
        for y in xrange(max_candidate, x - 1, -1):
            product = x * y
            if product <= biggest:
                break
            elif is_pallindrome(str(product)):
                biggest = product
    return biggest