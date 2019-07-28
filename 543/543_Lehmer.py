from bisect import bisect

def prime_sieve(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

limit = 10**6
primes = prime_sieve(limit)
print 'done with primes'

phi_cache = {}
def phi(x, a):
    if (x, a) in phi_cache:
        return phi_cache[(x, a)]
    if a == 1:
        return (x + 1) / 2
    val = phi(x, a-1) - phi(x // primes[a-1], a-1)
    phi_cache[(x, a)] = val
    return val

# Prime counting algorithm by Lehmer, 1959
# Adapted from 'Prime Numbers and Computer Methods for Factorization, 2nd ed.'
# by H. Riesel, Birkhauser 1994
# and http://stackoverflow.com/a/19072704

pi_cache = {}
def pi(x):
    if x in pi_cache: return pi_cache[x]
    if x < limit:
        val = bisect(primes, x)
        pi_cache[x] = val
        return val

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
    return int(my_sum)

def S(n):
    # Edge case
    if n == 3: return 2

    # Contribution from even terms
    total = ((n/2) - 1)*(n/2)/2 + 1

    # Contribution from odd terms
    total += ((n-1)/2 - 2)*((n-1)/2 - 1)/2 + 1
    total += pi(n) + pi(n-2) - 3

    return total

# Fibonacci generator
def fib(n):
    a, b = 0, 1
    for _ in xrange(n):
        yield a
        a, b = b, a + b

def validate():
    assert S(10) == 20
    assert S(100) == 2402
    assert S(1000) == 248838

def main(L):
    # Get Fibonacci numbers from 3 to L
    fibs = list(fib(L+1))[3:]
    # Sum over the values we want
    return sum(map(S, fibs))

if __name__ == '__main__':
    #validate()
    print main(44)
