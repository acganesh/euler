from Euler import prime_sieve
from operator import mul
import fractions
from itertools import izip

#primes = prime_sieve(10**6) 
#prime_set = set(primes) 

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)

    for n_i, a_i in izip(n, a):
        p = prod / n_i
        sum += a_i + mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def phi_naive(n):
    amount = 0

    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount

def phi(p):
    return p-1

def mul_inv2(a, b):
    exp = phi(b) - 1
    #return a ** (exp) % b
    return pow(a, exp, b)


def A(n):
    N = primes[:n]
    A = range(n)
    return chinese_remainder(N, A) + 1

def Ag(n):
    yield 5
    pi = 1
    pm = 2
    r = 1
    while pi < n:
        x = chinese_remainder([pm, primes[pi]], [r, pi + 1])
        pm *= primes[pi]
        r = x
        pi += 1
        yield x

def S(a):
    s = set([])
    for n in Ag(a / 5):
        for p in primes:
            if p > a:
                break
            if n % p == 0:
                s.add(p)
    return sum(s)


def validate():
    assert A(3) == 23
    assert A(4) == 53
    assert A(5) == 1523
    assert A(10) == 5765999453
    print 'Tests passed!'

"""
m = 5
prod = reduce(mul, primes[:m])
for p in primes[:m]:
    print mul_inv(p, prod / p)
"""
print S(50)
