from sympy import binomial as bin2
from Euler import factor
from math import sqrt
from collections import Counter


def prime_sieve(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return sieve, [2] + [i for i in xrange(3,n,2) if sieve[i]]

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

M = 10**4
sieve, primes = prime_sieve(M)


def is_prime(n):
    if n == 2: return True
    if n % 2 == 0: return False
    try:
        if sieve[n]: return True
    except:
        pass
    return False

def factor2(n):
    pfs = []
    if is_prime(n): return [(n, 1)]

    for p in primes:
        temp, exp = n, 0
        while temp % p == 0:
            temp //= p
            exp += 1
        if n % p == 0:
            pfs.append((p, exp))
        if p*p > n:
            if pfs == []: pfs.append((n, 1))
            break

    return pfs


def factor3(n):
    pfs = []
    if is_prime(n): return [(n, 1)]

    for p in primes:
        exp = 0
        if n % p == 0:
            while n % p == 0:
                n //= p
                exp += 1
            pfs.append((p, exp))
        if p*p > n:
            if n > 1:
                pfs.append((n, 1))
            break
    return pfs


# This implementation is buggy
# When factor4 is called for the same n multiple times,
# it returns wrong values.
fs = [Counter()]*10**7
def factor4(n):
    if fs[n]: return fs[n]
    pfs = Counter()
    if is_prime(n):
        pfs[n] = 1
        fs[n] = pfs
        return pfs

    for p in primes:
        exp = 0
        if n % p == 0:
            while n % p == 0:
                n //= p
                exp += 1
            pfs[p] = exp
        if fs[n]:
            return pfs + fs[n]
        if p * p > n:
            if n > 1:
                pfs[n] = 1
            break
    fs[n] = pfs
    return pfs


memo = {}
def bin1(n, k):
    if (n, k) in memo:
        return memo[(n, k)]

    if k == n: return 1
    if k > n: return 0
    d, q = max(k, n-k), min(k, n-k)
    num =  1
    for n in xrange(d+1, n+1): num *= n
    denom = 1
    for d in xrange(1, q+1): denom *= d

    val = num / denom
    memo[(n, k)] = val
    memo[(n, n-k)] = val
    return val

def get_exps(n):
    return list(x[1] for x in factor(n))

def get_exps2(n):
    return list(x[1] for x in fs[n])

def get_exps3(n):
    return list(x[1] for x in factor3(n))

def get_exps4(n):
    ctr = factor4(n)
    return list([v for k, v in ctr.iteritems()])


print factor3(50)
print factor4(50)
print '3', get_exps3(50)
print '4', get_exps4(50)
#es = [v for k, v in factor4(50).iteritems()]
#import pdb; pdb.set_trace()

#print 'test'

#fs = factor4(50)
#es = [v for k, v in fs.iteritems()]
#print es


"""
for i in xrange(50, 100):
    print i
    if get_exps3(i) != get_exps4(i):
        print 'failure', i
"""

def g(n):
    m = get_exps3(n)
    lim = sum(m)
    r = len(m)

    def f(n, k):
        total = 0
        # Exponents in pf
        for i in xrange(k):
            val = (-1)**i * bin1(k, i)
            prod = 1
            for j in xrange(1, r+1):
                prod *= bin1(m[j-1]+k-i-1,m[j-1])
            val = val*prod
            total += val
        return total

    return sum(f(n,k) for k in xrange(1, lim+1))


f2memo = {1:1}
def f2(n):
    if n in f2memo:
        return f2memo[n]
    i, total = 1, 0
    while True:
        if i * i > n:
            break
        if n % i == 0:
            total += f2(i)
            if i != n/i and n/i < n:
                total += f2(n/i)
        i += 1
    f2memo[n] = total
    return total


f3memo = {1:1}
def f3(n):
    if n in f3memo:
        return f3memo[n]
    i, total = 1, 0
    while True:
        if i * i > n:
            break
        if n % i == 0:
            total += g(i)
            if i != n/i and n/i < n:
                total += g(n/i)
        i += 1
    f3memo[n] = total
    return total



def validate():
    assert g(12) == 8
    assert g(48) == 48
    assert g(120) == 132

validate() #print g(12)
def main(N):
    for i in xrange(5, N):
        if f3(i) == i:
            print i


# OEIS: http://oeis.org/A163272
def main2():
    data = [0,1,48,1280,2496,28672,29808,454656,2342912,11534336,57409536,218103808]
    return sum(data)

#N = 10**10
#main(N)
print main2()
