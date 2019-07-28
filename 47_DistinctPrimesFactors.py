def num_prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return len(set(factors))

#print num_prime_factors(644)

consec = 0
n = 100000

num_primes = 4

while n <= 1000000:
    if num_prime_factors(n) == num_primes:
        if num_prime_factors(n+1) == num_primes:
            if num_prime_factors(n+2) == num_primes:
                if num_prime_factors(n+3) == num_primes:
                    print n
    if n % 10000 == 0: print n
    n = n+1
