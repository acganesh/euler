def sieve(n):
    """
    Generate the primes less than or equal to n using the sieve of
    Eratosthenes.
    """
    primes, sieve = [], [True] * (n + 1)
    for p in range(2, n + 1):
        if sieve[p]:
            primes.append(p)
            for i in range(p * p, n + 1, p):
                sieve[i] = False
    return primes


def pi(x):
    """
    Calculates the number of primes less than or equal to x.
    """
    return len(sieve(x))
