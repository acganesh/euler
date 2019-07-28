from collections import Counter
from itertools import product
from sympy import binomial

def factor_sieve(n):
    #sieve = [[] for x in xrange(n+1)]
    sieve = Counter()
    for x in xrange(2, n+1):
        if sieve[x] == 0:
            for y in xrange(x, n+1, x):
                exp = 1
                num = y
                while num % x == 0:
                    num //= x
                    exp += 1
                sieve[y] += (exp - 1)
    return sieve

fs = factor_sieve(10**5)

memo2 = {}
def partition(number, limit):
    if number in memo2:
        return memo2[number]
    answer = set()
    answer.add((number, ))
    for x in xrange(1, number):
        for y in partition(number - x, limit):
            if len(y) <= limit - 1:
                answer.add(tuple(sorted((x, ) + y)))
    memo2[number] = answer
    return answer

print partition(10, 4)
print partition(1000, 4)

# Todo make this efficiently mod out?
def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in xrange(1, min(k, n - k) + 1):
            ntok = (ntok*n)
            ktok = (ktok*t)
            n -= 1
        return ntok // ktok
    else:
        return 0

def partitions_leq(N):
    limit = N / 2
    parts = set([])
    for i in xrange(1, limit+1):
        part = partition(i)
        parts.update(part)
    return parts


memo = {}
def F(*args):
    s_args = tuple(sorted(args))
    if s_args in memo: return memo[s_args]
    freqs = Counter()
    for arg in args:
        freq = fs[arg]
        freqs[freq] += 1
    for k in freqs.keys():
        if k != 1 and freqs[k] % 2 == 1:
            val = 1
            memo[s_args] = val
            return val
    val = 2
    memo[s_args] = val
    return val

def main(n, k):
    total = 0
    for args in product(xrange(2, n+1), repeat=k):
        if F(*args) == 1:
            total += 1
    return total

