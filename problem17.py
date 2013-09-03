
digit_hash = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

def englishify(n):
    ones = n % 10
    n /= 10
    tens = n % 10
    n /= 10
    hundreds = n % 10
    n /= 10
    thousands = n

    words = []
    if thousands:
        words.extend([digit_hash[thousands], "thousand"])
    if hundreds:
        words.extend([digit_hash[hundreds], "hundred"])
    if (hundreds or thousands) and (tens or ones):
        words.append("and")
    if tens == 1:
        words.append("{0}".format(digit_hash[tens * 10 + ones]))
    else:
        if tens > 1:
            words.append("{0}".format(digit_hash[tens * 10]))
        if ones:
            words.append("{0}".format(digit_hash[ones]))
    return ''.join(words)

def count_chars(n):
    total = 0
    for x in xrange(1, n + 1):
        total += len(englishify(x))
    return total
