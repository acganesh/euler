from Euler import prime_sieve, factor
import itertools
from operator import mul
from bisect import bisect
import random


# Brute force answer - doesn't seem likely to be correct
# 564521188

# Answer with D3
#92622068

def sieve(l):
  s = [True] * (l + 1)
  s[0:2] = [False, False]
  for x in xrange(2, l):
    if s[x]:
        s[x ** 2::x] = [False] * ((l - x ** 2) / x + 1)
  return s

# Sieves for factorizations and primes
def factor_sieve(n):
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
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


def get_divisors(pf):
    expanded = []
    for x, exp in pf:
        e = ([x ** p for p in xrange(exp+1)])
        expanded.append(e)

    divisors = [reduce(mul, i, 1) for i in itertools.product(*expanded)]
    return divisors


#--- Miller-Rabin primality test----------------------------------------------------------------
def miller_rabin(n):
    """
    Check n for primalty:  Example:

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

lim = 10**6
sieve, factors = factor_sieve(lim)
primes = [x for x in xrange(lim) if sieve[x]]
print 'done sieveing'

# The old approach with standard sieve
#sieve = sieve(lim)
#primes = [x for x in xrange(lim) if sieve[x]]

# Only works for even $n$, which is fine
# because all of our candidates are multiples of 308.
#@profile
def D(k):
    target = 20010
    prod = 1

    for p in primes:
        if k % (p-1) == 0:
            prod *= p
            # if prod > target: return False
        if p-1 > k:
            break
    return prod

def D2(k):
    target = 20010
    prod = 1

    lim = bisect(primes, k+1)

    for p in primes[:lim]:
        if k % (p-1) == 0:
            prod *= p
            if prod > target:
                return False
    return prod

def D3(k):
    target = 20010
    prod = 1

    divisors = get_divisors(factor(k))

    for d in divisors:
        if is_prime(d+1):
            prod *= (d+1)
            if prod > target:
                return False

    return prod


def is_prime(n):
    if n < lim:
        return sieve[n]
    return miller_rabin(n)

# Test if n satisfies D(n) = 20010
# D2 seems slightly faster, but not by a huge amount
def is_valid(n):
    return D3(n) == 20010

#@profile
def F(m):

    # For composite multiples m, pre_check m
    # to see that m is a product of primes that are valid
    def pre_check(n):
        if n == 1 or is_prime(n):
            return True
        limit = int(n**.5) + 1
        for f in xrange(1, limit):
            if n % f == 0:
                f2 = n / f
            if not f in valid or not f2 in valid:
                return False
        return True

    def pre_check2(n):
        if n == 1 or is_prime(n):
            return True
        divisors = get_divisors(factors[n])
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
        if pre_check2(num):
            if is_valid(num):
                valid.add(factor)
                # print count, '308*%s' % factor, num
                if count % 1000 == 0: print count
                count += 1
            factor += 1
    return num

def tests():
    assert D3(4) == 30
    assert D3(308) == 20010
    assert F(1) == 308
    assert F(10) == 96404

tests()


#print D3(4)
#print D3(308)
#print F(10)
#print F(10000)
print F(100000)
#print F(10000)
#print F(100000)


#for i in range(1, 20): print i, D(i), D(308), D(308*i)
#print D(4)
#print F(1)
