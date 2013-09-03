
path_cache = {}

def collatz_length_starting_at(n):
    link = n;
    length = 1;
    while link > 1:
        if link in path_cache:
            length = path_cache[link] + length
            break
        length += 1
        link = link // 2 if link % 2 == 0 else 3 * link + 1
    path_cache[n] = length
    return length

def find_longest_chain_starting_under(n):
    maximum = 0;
    starting_number = 0;
    for x in xrange(n):
        length = collatz_length_starting_at(x)
        if length > maximum:
            maximum = length
            starting_number = x
    return starting_number, x
        