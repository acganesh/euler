import itertools
from operator import mul

# Factorize the first million integers using a sieve
def factor_sieve(n):
    sieve = [[] for x in xrange(n+1)]
    for x in xrange(2, n+1):
        if sieve[x] == []:
            for y in xrange(x, n+1, x):
                exp = 1
                num = y
                while num % x == 0:
                    num //= x
                    exp += 1
                sieve[y].append((x, exp-1))
    return sieve

# Sieves for factorizations and primes
def factor_sieve2(n):
    sieve = [True] * (n+1)
    factors = [[] for x in xrange(n+1)]
    for x in xrange(2, n+1):
        if sieve[x]:
            for y in range(x, n+1, x):
                exp = 1
                num = y
                while num % x == 0:
                    num //= x
                    exp += 1
                factors[y].append((x, exp-1))
                if y > x:
                    sieve[y] = False
    return sieve, factors

# Useful function to expand prime factorization
# into set of divisors
def get_divisors(pf):
    expanded = []
    for x, exp in pf:
        e = ([x ** p for p in xrange(exp+1)])
        expanded.append(e)

    divisors = set([reduce(mul, i, 1) for i in itertools.product(*expanded)])
    return divisors

sieve, factors = factor_sieve2(100)
import pdb; pdb.set_trace()

# This algorithm doesn't quite work, as it sieves for only divisors
# that are prime powers.
def faulty_divisor_sieve(n):
    sieve = [set([]) for x in xrange(n+1)]
    for x in xrange(2, n+1):
        if sieve[x] == set():
            for y in xrange(x, n+1, x):
                exp = 0
                num = y
                while num % x == 0:
                    num //= x
                    exp += 1
                    sieve[y].add(x**exp)
    return sieve


# Basic prime sieve - the one in Euler.py
# is more efficient
def sieve(n):
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n+1):
        if sieve[p]:
            ps.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return ps
