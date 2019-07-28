#from sympy import binomial
from operator import mul
from fractions import Fraction
from decimal import *

from math import floor, log

def binomial(n, k):
    """Computes nCk binomial coefficient."""
    return int( reduce(mul, (Fraction(n-i, i+1) for i in range(k)), 1) )

memo = {}
def g(m, n, b):
    if (m, n, b) in memo:
        return memo[(m, n, b)]
    # Base case
    if m < 0: return 0
    elif m == 0 or n == 0: return 1
    # Recurse
    elif m >= n:
        val = sum([g(m-k, n, b) * binomial(n+1, k) * (-1)**(k+1) for k in range(1, n+2)])
        memo[(m, n, b)] = val
        return int(val)
    else:
        val = g(m-1, n, b) + g(b*m, n-1, b)
        memo[(m, n, b)] = val
        return int(val)


def f0(k, n):
    """Old function for testing."""
    if n < k: return n+1
    return f0(k, n-1) + f0(k, n/k)


def num_digits(n, b):
    """Returns the number of digits in the base b representation of n."""
    return int(floor(log(n, b))) + 1

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n /= b
    return digits[::-1]

def a2(n, b):
    t = num_digits(n, b)
    #getcontext().prec = 10
    #return g(Decimal(n)/(b**(t-1)), t, b)
    return g(Fraction(n, b**(t-1)), t, b)

def tests():
    assert a2(10, 5) == 18
    assert a2(100, 7) == 1003
    assert a2(1000, 2) == 264830889564

    b = 2
    #for i in xrange(2, 100): assert a2(i, b) == f0(b, i)
    #This works for b = 2, but not higher bases, sadly
    print 'Tests passed!'


def main():
    mod = 10**9+7
    total = 0
    for i in range(2, 11):
        total += a2(10**14, i) % mod
        print 'Progress', i
    return total % mod

#getcontext().prec = 500
#for i in range(1, 30): print i, a2(i, 3), f0(3, i)
tests()
print main()
