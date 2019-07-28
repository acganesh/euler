from Euler import prime_sieve

# Expanding (p_n-1)^n + (p_n+1)^n with the binomial
# theorem, and modding out, note that $r$ can be expressed
# simply as follows:
# r = 2np_n when n is odd, and r = 2 when n is even.
# Thus, the problem is equivalent to finding the lowest n such that
# 2np_n > 10^{10}


def main(limit):
    primes = prime_sieve(10**7)

    for n, p in enumerate(primes):
        if n % 2 == 0 and 2*(n+1)*p > limit:
            return (n+1)

print main(10**10)
