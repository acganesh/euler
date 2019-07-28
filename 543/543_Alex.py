def sieve(l):
  s = [True] * (l + 1)
  s[0:2] = [False, False]
  for x in xrange(2, l):
    if s[x]:
        s[x ** 2::x] = [False] * ((l - x ** 2) / x + 1)
  return s

def sieve2(n):
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return sieve, [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

lim = 10
psieve = sieve(lim)
primes = [x for x in xrange(lim) if psieve[x]]

psieve2, primes2 = sieve2(lim)

print psieve == psieve2
print psieve
print psieve2
print primes == primes2

print "done with primes"

def isPrime(n):
    if n < lim:
        return psieve[n]
    for p in primes:
        if p * p > n:
            return True
        if n % p == 0:
            return False
    raise ValueError


def S(n):
    total = 8 + ((n / 2) - 1) * (n / 2) / 2 + (n / 2 - 2) * (n / 2 - 3) / 2 - 1
    for i in range(9, n + 1, 2):
        if isPrime(i):
            total += 2
        continue
    return total


def F(k):
    a, b = 0, 1
    c = 1
    while c < k:
        a, b = b, a + b
        c += 1
    return b

def main(l):
    total = 0
    for k in xrange(3, l + 1):
        s = S(F(k))
        print k, F(k), s
        total += s
    return total

#main(44)
