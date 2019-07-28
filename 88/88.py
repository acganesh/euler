from Euler import factor, prime_sieve
from operator import mul
from collections import defaultdict
import sys

def prod(*args):
    return reduce(mul, *args)

def is_valid(*args):
    return prod(*args) == sum(*args)

# Return all decompositions of n into factors
primes = prime_sieve(10**6)
prime_set = set(primes)

def is_prime(n):
    return n in prime_set

# Return all decompositions of n
memo = {}
def D(n):
    # Memoize
    if n in memo: return memo[n]

    vals = [(n, )]
    #vals = []

    # Base case
    if is_prime(n) or n == 1:
        memo[n] = vals
        return vals

    limit = int(n**.5)

    for i in xrange(2, limit+1):
        if n % i == 0:
            val = [(i,)+d for d in D(n/i)]
            vals += val
    memo[n] = vals
    return vals


# Calculate a specific value of P
def P(k):
    limit = 2*k
    min_k = sys.maxint
    min_n = sys.maxint
    for i in xrange(1, limit+1):
        ds = D(i)
        ks = [i - sum(d) + len(d) for d in ds]

        if k in ks and i < min_n:
            min_n = i

    return min_n

# Sum the first k (unique) values of P
def S(L):
    limit = 2*L
    vals = [0]*(L+1)

    for i in xrange(1, limit+1):
        ds = D(i)
        ks = [i - sum(d) + len(d) for d in ds]

        for k in ks:
            if 1 < k <= L:
                val = vals[k]
                if val == 0:
                    vals[k] = i
                else:
                    vals[k] = min(vals[k], i)

    return sum(set(vals))


def validate():
    assert P(2) == 4
    assert P(3) == 6
    assert P(4) == 8
    assert P(5) == 8
    assert P(6) == 12
    assert S(12) == 61

print S(12000)
