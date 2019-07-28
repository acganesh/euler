
def prime_sieve(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

#limit = 10**6
#primes = prime_sieve(limit)


def totient_sieve(n):
    t = range(n+1)
    sieve = [False]*(n+1)
    for x in xrange(2, n+1):
        if sieve[x] == False:
            t[x] = x-1
            for y in xrange(x, n+1, x):
                sieve[y] = True
                if y != x:
                    t[y] = t[y]*(x-1) // x
    return t

limit = 5*10**8
s = totient_sieve(limit)
print 'sieves done'

def f(n):
    if n % 2 == 0:
        return 0
    else:
        return s[n]

def g(n):
    return sum([f(n) for n in xrange(1, n+1, 2)])

print g(limit)
