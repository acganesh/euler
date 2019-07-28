def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

def sigma_2(n):
    pfs = prime_factors(n)
    pfs_set = set(pfs)

    prod = 1

    for item in pfs_set:
            exp = pfs.count(item)
            prod *= (item ** (2*(exp+1)) - 1)/(item ** 2 - 1)
            #prod *= ((item ** (2*(exp+1)) - 1)/(item ** 2 - 1) % (10 ** 9))
    return prod

def SIGMA_2_mod10e9(n):
    my_sum = 0
    for i in xrange(1, n+1):
        my_sum = (my_sum + sigma_2(i)) % (1000000000)
        if (i % 1000) == 0:
            print i
    return my_sum

pfs = prime_factors(1000)
print pfs

sig = sigma_2(6)
print sig

print SIGMA_2_mod10e9(4)
print SIGMA_2_mod10e9(5)

print SIGMA_2_mod10e9(1000000000000000L)

largest_prime_factor = max(pfs) # The largest element in the prime factor lis
