from itertools import product
from collections import Counter
from math import log, floor, ceil
from fractions import Fraction
from decimal import Decimal


def f(xs, cs, k, mod=None):
    """Returns (f(x_1, x_2, ..., x_n))^k for x_i in xs,
    where f is a polynomial with coefficients cs."""
    assert len(xs) == len(cs[1:])
    S = cs[0]  # Constant term
    if mod:
        S = S % mod
    for x, c in zip(xs, cs[1:]):
        if mod:
            S += x*c % mod
        else:
            S += x*c
        if mod:
            S = S % mod
    return long(pow(S, k, mod))

def f3(xs, cs, k, mod=None):
    S = 0
    for x, c in zip(xs, cs):
        S += x*c
        if mod:
            S = S % mod
    return pow(S, k, mod)


def f2(xs, cs, k, mod=None):
    """Returns (f(x_1, x_2, ..., x_n))^k for x_i in xs,
    where f is a polynomial with coefficients cs."""

    # Note -- this is not correct, because each
    # term in the generating function needs to have equal precedence
    # Thus, our representation will be a multivariable function
    assert len(xs) == len(cs[1:])
    S = cs[0]  # Constant term
    i = 1
    for x, c in zip(xs, cs[1:]):
        S += c*(x**i)
        i += 1
    return pow(S, k, mod)

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
    return cs


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
    """Computes the generating function, f(x_1, ..., x_r) corresponding to the
    (n, ku game's state space.  The number of winning positions
    for player 2 is equal to the sum of the terms in the expansion of
    f(x_1, ..., x_r)^k with even exponents for the x_i. Uses the principle of
    inclusion-exclusion to compute the desired sum of multinomial coefficients.
    """
    cs = get_coeffs(n)

    # Status check for long computations
    if n > 10**6: print 'Got coefficients'
    n_cs = len(cs)

    # Total game positions, equal to (n-1)**k
    T = f([1]*(n_cs-1), cs, k, mod)
    assert T == pow(n-1, k, mod)

    # This will represent the number of winning starting
    # positions for player 2.
    T2 = 0

    for xs in product([-1, 1], repeat=(n_cs-1)):
        # Testing variants on precision of this division
        # t = (n_cs-1-sum(xs))/2. + 1
        # t = Decimal(n_cs-1-sum(xs)) / Decimal(2) + 1
        #t = Fraction(n_cs-1-sum(xs), 2) + 1
        t = n_cs-1-sum(xs) / 2 + 1

        if mod:
            T2 = T2 + (-1)**t*T % mod
            T2 = T2 % mod
            T2 = T2 + f(xs, cs, k, mod)
            T2 = T2 % mod
        else:
            T2 = T2 + (-1)**t*(T + (-1)**t*f(xs, cs, k, mod))
    if mod:
        # Perform modulo division by computing modular inverse of 2**(n_cs-1)
        # In general, the modular inverse will exist when mod is odd.
        # We probably don't need this many mod operations
        T2 = T2*(modinv(pow(2, n_cs-1), mod) % mod) % mod
        # Compute the number of winning positions for player 1
        # by subtracting T2 from the total # of positions.
        T1 = T - T2
        return (T1 % mod)
    else:
        T1 = T - (T2 / pow(2, n_cs-1))
        return T1

# When using Fraction class:
# 902386361

# When using float div:
# 902386353

# When using Decimal class:
# Returns -85267960,
# but this is congruent to
# 902386361.


def main2(n, k, mod=None):
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
    assert T == pow(n-1, k, mod)

    # This will represent the number of winning starting
    # positions for player 2.
    T2 = 0

    """ For reference:
    for xs in product([-1, 1], repeat=(n_cs-1)):
        # Testing variants on precision of this division
        # t = (n_cs-1-sum(xs))/2. + 1
        # t = Decimal(n_cs-1-sum(xs)) / Decimal(2) + 1
        t = Fraction(n_cs-1-sum(xs), 2) + 1

        T2 = T2 + (-1)**t*(T + (-1)**t*f(xs, cs, k, mod))
        if mod: T2 = T2 % mod
    """
    for ts in product([-1, 1], repeat=(n_cs-1)):
        xs = [(-1)**t for t in ts]
        t = sum(ts)
        T2 = T2 + (-1)**t*(T + (-1)**t*f(xs, cs, k, mod))
        if mod: T2 = T2 % mod

    if mod:
        # Perform modulo division by computing modular inverse of 2**(n_cs-1)
        # In general, the modular inverse will exist when mod is odd.
        # We probably don't need this many mod operations
        T2 = T2*(modinv(pow(2, n_cs-1), mod) % mod) % mod
        # Compute the number of winning positions for player 1
        # by subtracting T2 from the total # of positions.
        T1 = T - T2
        return (T1 % mod)
    else:
        T1 = T - (T2 / pow(2, n_cs-1))
        return T1


def main3(n, k, mod=None):
    """
    Variant of main function that computes xs over the space [0, 1] x (n_cs -
    1).
    """
    cs = get_coeffs(n)

    # Status check for long computations
    if n > 10**6: print 'Got coefficients'
    n_cs = len(cs)
    #assert n_cs == int(floor(log(n, 2)))

    # Total game positions, equal to (n-1)**k
    T = f([1]*(n_cs-1), cs, k, mod)
    #assert T == pow(n-1, k, mod)

    # This will represent the number of winning starting
    # positions for player 2.
    T2 = 0

    """ For reference:
    for xs in product([-1, 1], repeat=(n_cs-1)):
        # Testing variants on precision of this division
        # t = (n_cs-1-sum(xs))/2. + 1
        # t = Decimal(n_cs-1-sum(xs)) / Decimal(2) + 1
        t = Fraction(n_cs-1-sum(xs), 2) + 1

        T2 = T2 + (-1)**t*(T + (-1)**t*f(xs, cs, k, mod))
        if mod: T2 = T2 % mod
    """
    for ts in product([0, 1], repeat=(n_cs-1)):
        xs = [(-1)**t for t in ts]
        T2 += f(xs, cs, k, mod)
        if mod: T2 = T2 % mod

    if mod:
        # Perform modulo division by computing modular inverse of 2**(n_cs-1)
        # In general, the modular inverse will exist when mod is odd.
        # We probably don't need this many mod operations
        T2 = T2*(modinv(pow(2, n_cs-1), mod) % mod) % mod
        # Compute the number of winning positions for player 1
        # by subtracting T2 from the total # of positions.
        T1 = T - T2
        return (T1 % mod)
    else:
        T1 = T - (T2 / pow(2, n_cs-1))
        return T1


def main4(n, k, mod=None):
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
    #T = f([1]*(n_cs-1), cs, k, mod)
    T = pow(n-1, k, mod)
    #assert T == pow(n-1, k, mod)

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
    for k in xrange(2, 20):
        print main4(10**7, k)
    """
    for k in range(2, 20):
        print main4(10, k)
    #print main4(10, 5)
    #validate()
    print 'old value', 902386361
    mod = 987654321
    print main4(long(pow(10,7)), long(pow(10,12)), long(mod))
    #print main3(10**7, 10**12, mod)
    """
