from sympy import binomial

memo = {}
def g(b, n):
    t = None
    if (b, n) in memo:
        return memo[(b, n)]
    if b < 0:
        return 0
    elif b == 0 or n == 0:
        return 1
    elif b >= n:
        val = sum([g(b-t, n) * binomial(n+1, t) * (-1)**(t+1) for t in xrange(1, n+2)])
        memo[(b, n)] = val
        return val
    else:
        val = g(b-1, n) + g(2*b, n-1)
        memo[(b, n)] = val
        return val


def a(n):
    t = len(bin(n)) - 2
    return g(float(n)/(2**(t-1)), t)


print a(10**14)
