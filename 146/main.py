from Euler import prime_sieve

primes = prime_sieve(10**8)
prime_set = set(primes)

def is_prime(k):
    return k**2+1 in prime_set

def f(n):
    vals = [n**2+k for k in [1, 3, 7, 9, 13, 27]]

    try:
        ind = primes.index(vals[0])
        if primes[ind:ind+6] == vals:
            return True
        else:
            return False

    except ValueError:
        return False

def tests():
    for k in xrange(9500):
        if f(k): print k

tests()
