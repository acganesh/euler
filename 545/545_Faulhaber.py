from Euler import prime_sieve, is_prime
from Euler import factor as factorize
from fractions import Fraction
from numpy import prod
import itertools
from operator import mul
from collections import Counter

# Akiyama-Tanigawa algorithm for Bernoulli_n
def bernoulli(n):
    A = [0]*(n+1)
    for m in xrange(n+1):
        A[m] = Fraction(1, (m+1))
        for j in xrange(m, 0, -1):
            A[j-1] = j*(A[j-1] - A[j])
    return A[0]

# Naive implementation of Bernoulli denominator
def D1(n):
    return bernoulli(n).denominator


# Efficient implementation of Bernoulli denominator,

def sieve(n):
    ps, sieve = [], [True] * (n + 1)
    for p in range(2, n+1):
        if sieve[p]:
            ps.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return ps



# Factorize the first million integers using a sieve
def factor_sieve(n):
    primes = []
    pfs = [[] for x in range(n+1)]
    for x in range(2, n+1):
        if pfs[x] == []:
            primes.append(x)
            for y in range(x, n+1, x):
                exp = 1
                num = y
                while num % x == 0:
                    num //= x
                    exp += 1
                pfs[y].append((x, exp-1))
                #sieve[y].append([x ** p for p in xrange(exp)])
    return primes, pfs


# Factorize the first million integers using a sieve
# Using Collections
@profile
def factor_sieve2(n):
    primes = []
    pfs = [Counter() for x in range(n+1)]
    for x in range(2, n+1):
        if pfs[x] == Counter():
            primes.append(x)
            for y in range(x, n+1, x):
                exp = 1
                num = y
                while num % x == 0:
                    num //= x
                    exp += 1
                pfs[y][x] = exp - 1
                #sieve[y].append([x ** p for p in xrange(exp)])
    return primes, pfs

def get_divisors2(pfs):
    all_divisors = []
    for pf in pfs:
        expanded = []
        for x, exp in pf:
            e = ([x ** p for p in xrange(exp+1)])
            expanded.append(e)

        # reduce(mul, i, 1) returns the product of an iterable
        divisors = set([reduce(mul, i, 1) for i in itertools.product(*expanded)])
        all_divisors.append(divisors)

    return all_divisors

def get_divisors(pf):
    expanded = []
    for x, exp in pf:
        e = ([x ** p for p in xrange(exp+1)])
        expanded.append(e)

    divisors = set([reduce(mul, i, 1) for i in itertools.product(*expanded)])
    return divisors


N = 10**5
M = 10
primes, pfs = factor_sieve2(N)
print 'done sieveing'


#print primes
#print pfs
#primes, pfs = factor_sieve(10**6)
#divisors = get_divisors(pfs)

def test_valid1(num, target):
    prod = 1

    for p in primes:
        if (num % (p-1) == 0):
            prod *= p
        if prod > target:
            break

    return prod == target

def test_valid2(num, target):
    prod = 1
    divs = get_divisors(pfs[num])
    for p in primes:
        if p-1 in divs:
            prod *= p
        if prod > target:
            break

    return prod == target

def merge_pf(pf):
    pf_308 = Counter({2: 2, 7:1, 11:1})
    return pf_308 + pf

def get_divisors3(pf):
    pf = merge_pf(pf)

    expanded = []
    for x, exp in pf.iteritems():
        e = ([x ** p for p in xrange(exp+1)])
        expanded.append(e)

    divisors = set([reduce(mul, i, 1) for i in itertools.product(*expanded)])
    return divisors

def test_valid3(factor, target):
    prod = 1
    # Need to change
    divs = get_divisors3(pfs[factor])
    for p in primes:
        if p-1 in divs:
            prod *= p
        if prod > target:
            break
    return prod == target

def F1(n):
    target = 20010

    base = 308
    factor = 1

    count = 0
    while count < n:
        num = base*factor

        if test_valid3(factor, target):
            count += 1
        factor += 1
    return num


print F1(M)

# Iterate through prime multiples of 308
def F2(n):
    target = 20010
    primes = prime_sieve(10**7)

    base = 308
    factor = 1

    count = 0
    for p in [1] + primes:
        num = base*p

        while True:
            factor = 2
            if test_valid1(num, primes, target):
                count += 1
                if count == n:
                    return num
                num = base*p*factor
                factor += 1
            else:
                break
        factor += 1


    return num

# Factorize the first million integers using a sieve
def divisor_sieve(n):
    sieve = [set([1, x]) for x in range(n+1)]
    for x in range(2, n+1):
        if sieve[x] == set([1, x]):
            for y in range(x, n+1, x):
                exp = 1
                num = y
                while num % x == 0:
                    sieve[y].add(x ** exp)
                    num //= x
                    exp += 1
    return sieve

def divisor_sieve2(n):
    sieve = [set([1, x]) for x in range(n+1)]
    for x in range(2, n+1):
        if sieve[x] == set([1, x]):
            for y in range(x, n+1, x):
                exp = 1
                num = y
                while y % x == 0:
                    x = x ** exp
                    sieve[y].add(x)
                    #num //= x
                    exp += 1
    return sieve

# Iterate through prime multiples of 308
def F3(n):
    target = 20010

    base = 308
    factor = 1
    primes = prime_sieve(10**7)

    count = 0
    for p in [1] + primes:
        factor = 1
        num = base*p*factor

        while True:
            if test_valid1(num, primes, target):
                print num, factorize(num)
                count += 1
                if count == n:
                    return num
                factor += 1
                num = base*p*factor
            else:
                break


    return num


