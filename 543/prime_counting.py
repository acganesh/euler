# Implements Mehler prime counting,
# adapted from
# http://stackoverflow.com/questions/19070911/feasible-implementation-of-a-prime-counting-function
# Unfortunately this code doesn't really work, since
# it runs into Python recursion limits.
import sys
from math import floor
from bisect import bisect
#sys.setrecursionlimit(10)

def prime_sieve(n):
    """
    Return a list of prime numbers from 2 to a prime < n. Very fast (n<10,000,000) in 0.4 sec.
    Algorithm & Python source: Robert William Hanks
    http://stackoverflow.com/questions/17773352/python-sieve-prime-numbers
    """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

limit = 10**5
primes = prime_sieve(limit)

phi_cache = {}
def phi(x, a):
    if (x, a) in phi_cache:
        return phi_cache[(x, a)]
    if a == 1:
        return (x + 1) / 2
    val = phi(x, a-1) - phi(x // primes[a-1], a-1)
    phi_cache[(x, a)] = val
    return val

pi_cache2 = {}
def pi2(x):
    if x in pi_cache2:
        return pi_cache2[x]
    if x < limit:
        val = bisect(primes, x)
        pi_cache2[x] = val
        return val
    a = pi(floor(x**(1./2)))
    val = phi(x, a) + a - 1
    pi_cache2[x] = val
    return val

pi_cache = {}
def pi(x):
    if x in pi_cache: return pi_cache[x]
    if x < limit:
        val = bisect(primes, x)
        pi_cache[x] = val
        return val
    #a = pi(floor(x ** (1./4)))
    #b = pi(floor(x ** (1./2)))
    #c = pi(floor(x ** (1./3)))

    a = pi(x ** (1./4))
    b = pi(x ** (1./2))
    c = pi(x ** (1./3))

    my_sum = phi(x,a) + (b+a-2) * (b-a+1) / 2.
    for i in xrange(a+1, b+1):
        w = x / primes[i-1]
        lim = pi(w ** (1./2))
        my_sum = my_sum - pi(w)
        if i <= c:
            for j in xrange(i, lim+1):
                my_sum = my_sum - pi(w / primes[j-1]) + j - 1
    pi_cache[x] = my_sum
    return my_sum

print pi(10**8)
