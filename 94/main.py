from math import sqrt


def T(n):
    """Return nth triangular number."""
    return n*(n+1)/2

def main(limit):
    total = 0
    sq_limit = int(sqrt(limit)) + 1
    for n in xrange(1, sq_limit):
        for m in xrange(n+1, sq_limit):
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            #print a, b, c

            if abs(c-2*b) <= 1:
                per = 2*(b+c)
                total += per
            elif abs(c-2*a) <= 1:
                per = 2*(a+c)
                total += per

            if 2*(b+c) > limit and 2*(a+c) > limit:
                break
    return total

print main(10**9)
