from math import sqrt, floor, pi
from fractions import gcd
def main(N):
    ctr = 0

    num1 = float(2*N)
    denom1 = 1+(1+sqrt(2))**2

    lim1 = int(floor(sqrt(num1/denom1)))

    for i in xrange(1, int(lim1)+1):
        if i % 2 == 1:
            n1 = int(floor(i/sqrt(2)) + 1)
            nv = int(floor((sqrt(2*N-i**2)-i)/2))
            for j in xrange(n1, nv+1):
                if gcd(i, j) == 1:
                    ctr += 1

    num2 = float(N)
    denom2 = denom1

    lim2 = int(floor(sqrt(num2/denom2)))
    for i in xrange(1, lim2+1):
        n1 = int(floor(i*sqrt(2))+1)
        nv = int(floor(sqrt(N-i**2))-i)

        for j in xrange(n1, nv+1):
            if j % 2 == 1:
                if gcd(i, j) == 1:
                    ctr += 1

    return ctr

def main2(N):
    return N / (2*pi)

P = '3141592653589793'

for i in range(1, len(P)):
    val = int(P[:i])

    m1 = main(val)
    m2 = main2(val)
    print val, m1, m2, m2-m1


#print repr(main2(3141592653589793))
#print main(10**10)
#print main2(10**10)

