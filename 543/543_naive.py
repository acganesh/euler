def prime_sieve(n):
    """
    Return a list of prime numbers from 2 to a prime < n. Very fast (n<10,000,000) in 0.4 sec.
    
    Example:
    >>>prime_sieve(25)
    [2, 3, 5, 7, 11, 13, 17, 19, 23]

    Algorithm & Python source: Robert William Hanks

http://stackoverflow.com/questions/17773352/python-sieve-prime-numbers

    """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]
primes = prime_sieve(1000)
prime_set = set(primes)


def is_prime(n):
    return n in prime_set

memo = {}
def P(i, k):
    if (i, k) in memo:
        return memo[(i, k)]
    if k == 0:
        return False
    if k == 1 and is_prime(i):
        return True
    for p in primes:
        if p > i / k:
            break
        if P(i - p, k - 1):
            memo[(i-p, k-1)] = True
            return True
    memo[(i, k)] = False
    return False

def S(n):
    my_sum = 0
    for i in range(1, n+1):
        for k in range(1, n+1):
            Pv = P(i, k)
            my_sum += Pv
    return my_sum

def S2(n):
    # Even contribution
    total = (n/2 - 1)*(n/2)/2 + 1

    # Odd contribution
    total +=  ( (n-1) / 2 - 2)*( (n-1)/2 - 1) / 2 + 1

    # Compute terms for is_prime contributions
    prime_terms = 2*sum([is_prime(i) for i in range(5, n-2, 2)])
    prime_terms += is_prime(3) + is_prime(2*((n-1)/2)+1)

    total += prime_terms

    return total

for i in range(1, 15):
    print i, S(i)
