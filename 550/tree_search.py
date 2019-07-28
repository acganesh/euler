from math import sqrt
from itertools import product
from Euler import prime_sieve

def prime_sieve(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return sieve, [2] + [i for i in xrange(3,n,2) if sieve[i]]

limit = 10**6
sieve, primes = prime_sieve(limit)
#print 'done with primes!'

def is_prime(n):
    if n == 2: return True
    if n % 2 == 0: return False
    if n < limit:
        return sieve[n]
    else:
        return is_prime2(n)

def is_prime2(n):
    n = int(n)
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n < 9: return True
    if n%3 == 0: return False
    r = int(sqrt(n))
    f = 5
    while f <= r:
        if n%f == 0: return False
        if n%(f+2) == 0: return False
        f +=6
    return True

def get_divisors(n):
    for x in xrange(2, int(sqrt(n)) + 1):
        if n % x == 0:
            yield x
            if x != n / x:
                yield n / x

def switch(player):
    if player == 1: return 2
    elif player == 2: return 1


memo = {}
def F(player, *args):
    if (player, args) in memo:
        return memo[(player, args)]
    if all(map(is_prime, args)):
        return switch(player)
    else:
        vals = []
        args = list(args)
        for k in xrange(len(args)):
            val = args[k]
            divs = list(get_divisors(val))
            for d1, d2 in product(divs, repeat=2):
                new_args = [d1, d2] + args[:k] + args[k+1:]
                vals = vals + [F(switch(player), *new_args)]
        if player == 1:
            result = 1 if 1 in vals else 2
            memo[(player, tuple(args))] = result
            return result
        elif player == 2:
            result = 2 if 2 in vals else 1
            memo[(player, tuple(args))] = result
            return result

def main(n, k):
    total = 0
    for args in product(range(2, n+1), repeat=k):
        if F(1, *args) == 1:
            total += 1
    return total

if __name__ == '__main__':
    print main(10, 5)
