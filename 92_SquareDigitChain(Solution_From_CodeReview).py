import datetime

start = datetime.datetime.now()

''' V1 time: 43s
def square_digits(n):
    """Return the sum of squares of the base-10 digits of n."""
    total = 0
    for digit in str(n):
        total += int(digit) ** 2
    return total
'''

#Using ints is faster.  V2 time: 17.8s
def square_digits(n):
    """Return the sum of squares of the base-10 digits of n."""
    total = 0
    while n:
        total += (n % 10) ** 2
        n //= 10
    return total

def problem92a(limit):
    """Return the count of starting numbers below limit that eventually arrive
    at 89, as a result of iterating the sum-of-squares-of-digits.

    """
    arrive = [None] * limit # Number eventually arrived at, or None if unknown.
    arrive[1], arrive[89] = 1, 89
    for n in range(2, limit):
        chain = [n]
        while arrive[chain[-1]] is None:
            chain.append(square_digits(chain[-1]))
        for term in chain:
            if arrive[term] is None:
                arrive[term] = arrive[chain[-1]]
    return arrive.count(89)

#V3: avoid lookup of chain[-1] by storing in memory
#Reduce size of chain by one, because last element in chain is remembered already
#Checking if arrive[term] is None is unnecessary: we already know that last term in chain was found
#Time: 15.2s
def problem92b(limit):
    """Return the count of starting numbers below limit that eventually arrive
    at 89, as a result of iterating the sum-of-squares-of-digits.

    """
    arrive = [None] * limit # Number eventually arrived at, or None if unknown.
    arrive[1], arrive[89] = 1, 89
    for n in range(2, limit):
        chain = []
        while not arrive[n]:
            chain.append(n)
            n = square_digits(n)
        dest = arrive[n]
        for term in chain:
            arrive[term] = dest
    return arrive.count(89)

#V4: Max sum of squares is sum_of_squares(9999999) = 567
#For 568 and up, no need to follow the chain, we can just look up the answer directly.
#Time: 12.5s

def problem92c(limit):
    """Return the count of starting numbers below limit that eventually arrive
    at 89, as a result of iterating the sum-of-squares-of-digits.

    """
    sum_limit = len(str(limit - 1)) * 9 ** 2 + 1
    arrive = [None] * sum_limit
    arrive[1], arrive[89] = 1, 89
    for n in range(2, sum_limit):
        chain = []
        while not arrive[n]:
            chain.append(n)
            n = square_digits(n)
        dest = arrive[n]
        for term in chain:
            arrive[term] = dest
    c = arrive.count(89)
    for n in range(sum_limit, limit):
        c += arrive[square_digits(n)] == 89
    return c

from collections import Counter
from math import factorial
#from memoize import memoized

def partitions(n, k, v):
    """Return partitions of n into at most k items from v, with
    repetition. v must be a tuple sorted into numerical order. Each
    partition is returned as multiset in the form of a Counter object
    mapping items from v to the number of times they are used in the
    partition.

        >>> partitions(4, 7, (1, 4))
        [Counter({1: 4}), Counter({4: 1})]

    """
    if n == 0:
        # Base case: the empty partition.
        return [Counter()]
    if k == 0 or len(v) == 0 or n < v[0]:
        # No partitions possible here.
        return []
    pp = [p.copy() for p in partitions(n - v[0], k - 1, v)]
    for p in pp:
        p[v[0]] += 1
    return pp + partitions(n, k, v[1:])

def multinomial(n, k):
    """Return the multinomial coefficient n! / k[0]! k[1]! ... k[m]!.

        >>> multinomial(6, (2, 2, 2))
        90

    """
    result = factorial(n)
    for i in k:
        result //= factorial(i)
    return result

def number_count(digit_counts, min_digits, max_digits):
    """Return the count of numbers (with between min_digits and max_digits
    inclusive) whose distinct non-zero digits have counts given by the
    sequence digit_counts. For example if we have three identical
    non-zero digits and four digits in total:

        >>> number_count((3,), 4, 4)
        3

    because the possible numbers resemble 1011, 1101, and 1110.
    Similarly

        >>> number_count((1,1), 4, 4)
        6

    because the possible numbers resemble 1002, 1020, 1200, 2001,
    2010, and 2100.

    """
    nonzero_digits = sum(digit_counts)
    total = 0
    for digits in range(max(min_digits, nonzero_digits), max_digits + 1):
        for i, d in enumerate(digit_counts):
            counts = (digit_counts[:i] + (d - 1,) + digit_counts[i+1:]
                      + (digits - nonzero_digits,))
            total += multinomial(digits - 1, tuple(sorted(counts)))
    return total

def problem92d(limit):
    """Return the count of starting numbers below limit that eventually arrive
    at 89, as a result of iterating the sum-of-squares-of-digits.

    """
    max_digits = len(str(limit - 1))
    assert(limit == 10 ** max_digits) # algorithm works for powers of 10 only
    sum_limit = max_digits * 9 ** 2 + 1
    arrive = [None] * sum_limit
    arrive[1], arrive[89] = 1, 89
    for n in range(2, sum_limit):
        chain = []
        while not arrive[n]:
            chain.append(n)
            n = square_digits(n)
        dest = arrive[n]
        for term in chain:
            arrive[term] = dest
    total = 0
    squares = tuple(i ** 2 for i in range(1, 10))
    for n in range(2, sum_limit):
        if arrive[n] == 89:
            for p in partitions(n, max_digits, squares):
                total += number_count(tuple(sorted(p.values())), 1, max_digits)
    return total

#V5: New algorithm! Time: 0:00:02.623200
print problem92d(10000000)
print "Time elapsed", datetime.datetime.now() - start