import sys


memo = {}
mem = {}
mod = (10 ** 7) + 2

memo = {}
def f(k, n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    val = sum(f0(k, i / k) for i in range(n + 1))
    memo[n] = val
    return val

c, d = 0, 0
def f0(k, n):
    if n in memo:
        return memo[n]
    if n < k:
        return n + 1
    val = f(k, n - 1) + f(k, n / k)
    memo[n] = val
    return val

mem = {}
def f2(m, n, k=1):
    if (m, n) in mem:
        return mem[(m, n)]
    if n == 1:
        return k + 1
    if k == 0:
        return 1
    a = f2(m, n, k - 1) + f2(m, n - 1, k * m) % mod
    #a = f1(m, m**(n-1)) + f2(m, n-1, k*m)
    mem[(m, n)] = a
    return a

#tests(f0)
def f1(k, n):
    global memo
    global c, d
    c += 1
    if n in memo:
        d += 1
        return memo[n]
    if n < k:
        memo[n] = n + 1
        return n + 1
    lim = (n + (k - n % k) - 1)
    ans = 0
    for m in range(0, lim / k + 1):
        ans += f0(k, m)
    ans *= k
    sub = f0(k, lim / k)
    ans = ans - sub * (lim - n)
    memo[n] = ans# % memod
    return memo[n]


#print 2**2, f0(2, 2**2), f0(3, 2**2), f0(4, 2**2), f0(5, 2**2), f0(6, 2**2)
#print 3**3, f0(2, 3**3), f0(3, 3**3), f0(4, 3**3), f0(5, 3**3), f0(6, 3**3), f0(7, 3**3), f0(8, 3**3)

for i in range(2, 10):
    print f0(2, i)
#tests(f0)
