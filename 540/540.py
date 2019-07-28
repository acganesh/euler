from math import sqrt
from fractions import gcd


def main(limit):
    total = 0
    rt_limit = int(sqrt(limit)) + 1

    for n in xrange(1, rt_limit):
        for m in xrange(n+1, rt_limit, 2):
            c = m**2+n**2

            if c >= limit:
                break
            if gcd(m, n) == 1:
                #print a, b, c
                total += 1

    return total

for i in range(0, 10):
    print 'i = ', i, 'P(10^i)= ', main(10**i)
