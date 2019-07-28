from itertools import product
from math import sqrt
from collections import Counter
#from numpy import bitwise_xor
from operator import xor


def factor_sieve(n):
    """Sieve to calculate the number of prime factors in the
    factorizations of the integers from 1 to n."""
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

def S(position):
    position = list(position)
    successors = set()
    for k, val in enumerate(position):
        divs = list(get_divisors(val))
        for d1, d2 in product(divs, repeat=2):
            new_vals = [d1, d2] + position[:k] + position[k+1:]
            successors.add(tuple(new_vals))
    return successors

def get_divisors(n):
    for x in xrange(2, int(sqrt(n)) + 1):
        if n % x == 0:
            yield x
            if x != n / x:
                yield n / x

def mex(s):
    ans = 0
    while ans in s:
        ans += 1
    return ans

memo = {}

memo2 = {}
def bitwise_xor(a, b):
    if (a, b) in memo2:
        return memo2[(a, b)]
    if (b, a) in memo2:
        return memo2[(b,a)]
    else:
        val = a^b
        memo2[(a,b)] = val
        return val

def grundy(position):
    tsp = tuple(sorted(position))
    if tsp in memo: return memo[tsp]

    if len(position) == 1:
        s = set()
        for successor in S(position):
            s.add(grundy(successor))
        val = mex(s)
    else:
        vals = []
        for p in position:
            vals.append(grundy([p]))
        val = reduce(bitwise_xor, vals)

    memo[tsp] = val
    return val

memo = {}

fs = factor_sieve(10**6)

# This isn't quite correct.
def grundy2(position):
    if len(position) == 1:
        return fs[position[0]] - 1
    else:
        tsp = tuple(sorted(position))
        if tsp in memo: return memo[tsp]

        vals = []
        for p in position:
            vals.append(grundy2([p]))
        val = reduce(bitwise_xor, vals)

        memo[tsp] = val
        return val



def main(n, k):
    T1 = 0
    for position in product(xrange(2, n+1), repeat=k):
        if grundy2(position) > 0:
            T1 += 1
    return T1

def test():
    print grundy2([2]*10**8)

def test2():
    for k in xrange(2, 100):
        if grundy([k]) != grundy2([k]):
            print k, grundy([k]), grundy2([k])

#test()
#test2()
for k in range(2, 10): print main(10, k)

#print xor_grundy([2,3,2,5,6])
