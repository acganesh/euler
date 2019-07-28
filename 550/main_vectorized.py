from itertools import product
from collections import Counter
from math import log, floor, ceil
from fractions import Fraction
from decimal import Decimal

import numpy as np


def p(x,e,m):
    X = x
    E = e
    Y = 1
    while E > 0:
        if E % 2 == 0:
            X = (X * X) % m
            E = E/2
        else:
            Y = (X * Y) % m
            E = E - 1
    return Y

def f(xs, cs, k, mod=None):
    """Returns (f(x_1, x_2, ..., x_n))^k for x_i in xs,
    where f is a polynomial with coefficients cs."""
    assert len(xs) == len(cs[1:])
    S = cs[0]  # Constant term
    xs = np.asarray(xs)
    S += np.dot(xs, cs[1:])
    if mod:
        S = S % mod
    #S = int(S)
    S = long(S)
    #S = np.int64(S)
    if mod:
        return pow(S, k, mod)
    else:
        return pow(S, k)

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


def get_coeffs(n):
    """Get the coefficients of the generating function
    for an (n, k) divisor game.  This uses a sieve
    to factor the first n integers."""
    fs = factor_sieve(n)
    num = int(floor(log(n, 2)))
    #num = int(ceil(log(n, 2)))
    cs = [0]*num
    for _, v in fs.iteritems():
        cs[v-1] += 1
    return np.asarray(cs)


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    """Calculate the modular inverse of a mod m."""
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


def main(n, k, mod=None):
    """
    Variant of main function that computes xs over the space [0, 1] x (n_cs -
    1).
    """
    cs = get_coeffs(n)

    # Status check for long computations
    if n > 10**6: print 'Got coefficients'
    n_cs = len(cs)
    assert n_cs == int(floor(log(n, 2)))

    # Total game positions, equal to (n-1)**k
    T = f([1]*(n_cs-1), cs, k, mod)
    #T = pow(n-1, k, mod)
    assert T == pow(n-1, k, mod)

    # This will represent the number of winning starting
    # positions for player 2.
    T2 = 0

    for xs in product([-1, 1], repeat=n_cs-1):
        # Testing variants on precision of this division
        # t = (n_cs-1-sum(xs))/2. + 1
        # t = Decimal(n_cs-1-sum(xs)) / Decimal(2) + 1

        #T2 = T2 + pow(-1, t)*(T) + f(xs, cs, k, mod)
        T2 = T2 + f(xs, cs, k, mod)
        if mod: T2 = T2 % mod
    """
    for ts in product([0, 1], repeat=(n_cs-1)):
        xs = [(-1)**t for t in ts]
        t = sum(ts)
        T2 = T2 + (-1)**t*(T + (-1)**(t+1)*f2(xs, cs, k, mod))
        if mod: T2 = T2 % mod
    """

    if mod:
        # Perform modulo division by computing modular inverse of 2**(n_cs-1)
        # In general, the modular inverse will exist when mod is odd.
        # We probably don't need this many mod operations
        #T2 = T2*(modinv(pow(2, n_cs-1), mod) % mod) % mod
        # Old version
        """
        T2 = modinv(pow(2, n_cs-1), mod) * T2
        T2 = T2 % mod
        T1 = T - T2
        return (T1 % mod)
        """

        power = pow(2, n_cs-1)
        val = power*T - T2
        return (val * modinv(power, mod)) % mod
        # Compute the number of winning positions for player 1
        # by subtracting T2 from the total # of positions.
        #return T2
    else:
        #return T2 / pow(2, n_cs-1)
        T1 = T - (T2 / pow(2, n_cs-1))
        return T1


def test(n, k):
    print main3(n, k), main(n, k)
    #assert main3(n, k, 103) == main4(n, k, 103)

def validate():
    assert main3(10, 5) == 40085
    print 'Tests passed!'


if __name__ == '__main__':
    for k in range(2, 20):
        print main(10, k)
    print 'old value', 902386361
    mod = 987654321
    print main(long(pow(10,7)), long(pow(10,12)), long(mod))
    #print main3(10**7, 10**12, mod)

