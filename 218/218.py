from math import sqrt
from fractions import gcd


def is_square(n):
    rt = sqrt(n)
    return int(rt) == rt

def is_perfect(c):
    return is_square(c)

def is_super_perfect(a, b):
    # This is guaranteed to be integral by Euclid's formula
    area = a*b/2
    return area % 6 == 0 and area % 28 == 0

def main(N):
    total = 0
    lim = int(sqrt(N)) + 1
    for n in xrange(1, lim):
        for m in xrange(n+1, lim, 2):
            # Ensure that triples are primitive
            if gcd(m, n) == 1:
                a = m**2-n**2
                b = 2*m*n
                c = m**2+n**2
                if is_perfect(c) and not is_super_perfect(a, b):
                    import pdb; pdb.set_trace()
                    total += 1
                    print a, b, c
    return total

main(10**9)
