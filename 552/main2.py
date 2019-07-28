import math

def sieve(l):
  s = [True] * (l + 1)
  s[0:2] = [False, False]
  for x in range(2, l):
    if s[x]:
        s[x ** 2::x] = [False] * ((l - x ** 2) / x + 1)
  return s

l = 300000
psieve = sieve(l)
primes = [x for x in range(l) if psieve[x]]
prime_set = set(primes)

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)

    for n_i, a_i in zip(n, a):
        p = prod / n_i
        """
        if n_i in prime_set:
            sum += a_i * mul_inv2(p, n_i) * p
        else:
        """
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod



def phi(p):
    return p-1

def mul_inv2(a, b):
    exp = phi(b) - 1
    #return a ** (exp) % b
    return pow(a, exp, b)

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a / b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def Ag(n):
    yield 5
    pi = 1
    pm = 2
    r = 1
    while pi < n:
        x = chinese_remainder([pm, primes[pi]], [r, pi + 1])
        pm *= primes[pi]
        r = x
        pi += 1
        yield x

def S(a):
    s = set([])
    for n in Ag(a / 5):
        for p in primes:
            if p > a:
                break
            if n % p == 0:
                s.add(p)
    return sum(s)

print S(2000)
