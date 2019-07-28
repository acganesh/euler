from bisect import bisect

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

# Limit is F_{44} + 1
limit = 701408733+1
primes = prime_sieve(limit)
print 'done sieveing'

def pi(x):
    return bisect(primes, x)

def S(n):
    # Edge case
    if n == 3: return 2

    # Contribution from even terms
    total = ((n/2) - 1)*(n/2)/2 + 1

    # Contribution from odd terms
    total +=  ((n-1) / 2 - 2)*((n-1)/2 - 1) / 2 + 1
    total += pi(n) + pi(n-2) - 3

    return total

# Fibonacci generator
def fib(n):
    a, b = 0, 1
    for _ in xrange(n):
        yield a
        a, b = b, a + b

def main(L):
    # Get Fibonacci numbers from 3 to L
    fibs = list(fib(L+1))[3:]
    # Sum over the values we want
    return sum(map(S, fibs))

print main(44)
