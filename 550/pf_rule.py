from collections import Counter
from itertools import product

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
print 'done sieving'

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
