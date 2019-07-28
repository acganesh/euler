from math import factorial, floor, log

def prime_sieve(n):
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return sieve, [2] + [i for i in xrange(3,n,2) if sieve[i]]

sieve, primes = prime_sieve(10**6)

def is_prime(n):
    if n == 2: return True
    if n % 2 == 0: return False
    try:
        if sieve[n]: return True
    except:
        pass
    return False

def factor3(n):
    pfs = []
    if is_prime(n): return [(n, 1)]

    for p in primes:
        exp = 0
        if n % p == 0:
            while n % p == 0:
                n //= p
                exp += 1
            pfs.append((p, exp))
        if p*p > n:
            if n > 1:
                pfs.append((n, 1))
            break
    return pfs

def s(n):
    m = 1
    while True:
        if factorial(m) % n == 0:
            return m
        m += 1

# Modded version of s
def s2(n):
    m = 1
    fact = 1
    while True:
        m = (m * fact) % n
        if m == 0:
            return fact
        fact += 1

memo = {}
def a(p, j):
    if (p, j) in memo: return memo[(p, j)]
    if j == 1:
        memo[(p, j)] = 1
        return 1
    else:
        val = p*a(p, j-1) + 1
        memo[(p, j)] = val
        return val

def a(p, j):
    return (p**j - 1)/(p-1)

def v(p, alpha):
    return int(floor(log(1+alpha*(p-1), p)))


# Compute s(n) according to Kempner's algorithm
def s3(n):
    pf = factor3(n)
    max_val = 0
    for p, alpha in pf:
        v_val = v(p, alpha)

        ks = []
        rs = []

        ind = v_val

        k_v = alpha/a(p,v_val)
        r_v = alpha - k_v*a(p,v_val)
        
        import pdb; pdb.set_trace()

        ks.append(k_v)
        rs.append(r_v)

        ind = v_val+1
        while True:
            r = ks[-1]*a(p, ind-1) + rs[-1]
            rs.append(r)
            k = r/a(p, ind)
            ks.append(k)
            if r == 0: break
        val = (p-1)*alpha + sum(ks)
    return val

print s2(8)
print s3(8)

def S(n):
    return sum(s2(i) for i in range(2, n+1))


