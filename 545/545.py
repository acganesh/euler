from Euler import prime_sieve, factor
import itertools
from bisect import bisect
import random

def prime_sieve(l):
    s = [True] * (l + 1)
    s[0:2] = [False, False]
    for x in xrange(2, l):
        if s[x]:
            s[x ** 2::x] = [False] * ((l - x ** 2) / x + 1)
    primes = [x for x in xrange(lim) if s[x]]
    return s, primes


def miller_rabin(n):
    """
    Check n for primality:  Example:

    >miller_rabin(162259276829213363391578010288127)    #Mersenne prime #11
    True

    Algorithm & Python source:

http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)

    """
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1


lim = 10**7
sieve, primes = prime_sieve(lim)
print 'done sieving'


# From http://stackoverflow.com/a/171784
def get_divisors(n):
    factors = factor(n)
    nfactors = len(factors)
    f = [0] * nfactors
    while True:
        yield reduce(lambda x, y: x*y, [factors[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return

def D(k):
    target = 20010
    prod = 1

    divisors = get_divisors(k)

    for d in divisors:
        if is_prime(d+1):
            prod *= (d+1)
            if prod > target:
                break

    return prod


def is_prime(n):
    if n < lim:
        return sieve[n]
    return miller_rabin(n)

# Test if n satisfies D(n) = 20010
def is_valid(n):
    return D(n) == 20010

#@profile
def F(m):
    # For composite multiples m, pre_check m
    # to see that m is a product of primes that are valid
    def pre_check(n):
        if n == 1 or is_prime(n):
            return True
        divisors = get_divisors(n)
        for f in divisors:
            if not f in valid and f < n:
                return False
        return True

    count = 0
    base = 308
    factor = 1

    valid = set([])

    while count < m:
        num = base*factor
        if pre_check(factor):
            if is_valid(num):
                valid.add(factor)
                # Progress:
                if count % 1000 == 0: print count
                count += 1
        factor += 1
    return num

def tests():
    assert D(4) == 30
    assert D(308) == 20010
    assert F(1) == 308
    assert F(10) == 96404

tests()
print F(100000)
