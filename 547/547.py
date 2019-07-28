import random
from math import sqrt, log, cos, pi
from fractions import gcd
from scipy.integrate import nquad
import ctypes

import numpy as np

# Expected distance between two points in
# rectangle of dimensions a x b

#lib = ctypes.CDLL('integrand.o')
#func = lib.f
#func.restype = ctypes.c_double
#func.argtypes = (ctypes.c_int, ctypes.c_double)

E_cache = {}
#@profile
def E(a, b):
    if (a,b) in E_cache:
        return E_cache[(a,b)]
    if (b,a) in E_cache:
        return E_cache[(b,a)]
    a = float(a)
    b = float(b)
    d = sqrt(a**2+b**2)
    val = 1./15*(a**3/b**2 + b**3/a**2 + d*(3 - a**2/b**2 - b**2/a**2) + 5./2*(b**2/a*log((a+d)/b) + a**2/b*log((b+d)/a)))
    E_cache[(a,b)] = val
    return val


# Returns Euclidean distance between two points
#@profile
def dist(P1, P2):
    return sqrt(sum( (x1 - x2)**2 for x1, x2 in zip(P1, P2)))

def dist2(P1, P2):
    return np.linalg.norm( [(x1 - x2) for x1, x2 in zip(P1, P2)])



#@profile
def T2(m, n, h):
    m = float(m)
    n = float(n)
    h = float(h)
    s = E(m + n, h)
    s -= ((n * h) / (n * h + m * h)) ** 2 * E(n, h)
    s -= ((m * h) / (n * h + m * h)) ** 2 * E(m, h)
    s /= 2 * ((m * h) / (n * h + m * h)) * ((n * h) / (n * h + m * h))
    return s

#@profile
def D(m, n, i, j):
    m = float(m)
    n = float(n)
    i = float(i)
    j = float(j)

    A = (m+i)*(n+j)
    val = E(m+i, n+j)
    # Multiplied this factor by 2 and things seem to work
    val -= 2*(((i*n)/A)**2*E(i, n) + ((j*m)/A)**2*E(j, m))
    val -= 2*((j*m)*(n*m)/A**2)*T2(n,j,m)
    val -= 2*((i*n)*(i*j)/A**2)*T2(n,j,i)
    val -= 2*((n*m)*(i*n)/A**2)*T2(m,i,n)
    val -= 2*((i*j)*(j*m)/A**2)*T2(m,i,j)

    R = (j*m + i*n)/(m*n + i*j)
    #R = 1
    R = R ** .5
    val /= 2*(m*n)*(i*j)/A**2 + 2*(i*n)*(m*j)*R/A**2
    return val


cache = {}
#@profile
def Ds(m, n, i, j, num_iter):
    if (m, n, i, j) in cache:
        return cache[m, n, i, j]
    if (n, m, j, i) in cache:
        return cache[n, m, j, i]
    if (i, j, m, n) in cache:
        return cache[i, j, m, n]
    if (j, i, n, m) in cache:
        return cache[j, i, n, m]

    def get_point(a, b, c, d):
        x = random.uniform(a, b)
        y = random.uniform(c, d)
        return (x, y)

    total = 0

    for _ in xrange(num_iter):
        P1 = get_point(0, m, 0, n)
        P2 = get_point(m, m+i, n, n+j)
        total += dist(P1, P2)

    val = total/float(num_iter)
    cache[(m, n, i, j)] = val

    return val

#@profile

def D_main(m, n, i, j):
    if m == i or n == j:
        return D(m, n, i, j)

    g = reduce(gcd, (m, n, i, j))

    if g > 1:
        return g*D_num(m/g, n/g, i/g, j/g)

    return D_num(m, n, i, j)

def integrand(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)


cache = {}
def D_num(m, n, i, j):
    if (m, n, i, j) in cache:
        return cache[m, n, i, j]
    if (n, m, j, i) in cache:
        return cache[n, m, j, i]
    if (i, j, m, n) in cache:
        return cache[i, j, m, n]
    if (j, i, n, m) in cache:
        return cache[j, i, n, m]
    m, n, i, j = map(float, (m, n, i, j))
    ranges = [(0, m), (0, n), (m, m+i), (n, n+j)]
    prec = {'epsrel': 1e-4, 'epsabs': 1e-4}
    val = nquad(integrand, ranges, opts=prec)
    result = 1./(m*n*i*j)*val[0]
    cache[(m, n, i, j)] = result
    return result


import time
start = time.time()


def S(s):
    e = 0
    A = s * s

    num = 0
    for x1 in range(1, s - 1):
        for y1 in range(1, s - 1):
            for x2 in range(x1 + 1, s):
                for y2 in range(y1 + 1, s):
                    c = 0
                    e0 = E(s, s)
                    m = x2 - x1
                    n = y2 - y1

                    m = float(m)
                    n = float(n)

                    #Left and Right adjacent
                    c += 2 * (m * n) * (x1 * n)
                    e0 -= 2 * T2(m, x1, n) * (m * n) / A * (x1 * n) / A
                    c += 2 * (m * n) * ((s - x2) * n)
                    e0 -= 2 * T2(m, s - x2, n) * (m * n) / A * ((s - x2) * n) / A
                    #Top and Bottom adjacent
                    c += 2 * (n * m) * (y1 * m)
                    e0 -= 2 * T2(n, y1, m) * (n * m) / A * (y1 * m) / A
                    c += 2 * (n * m) * ((s - y2) * m)
                    e0 -= 2 * T2(n, s - y2, m) * (n * m) / A * ((s - y2) * m) / A
                    #Top Left
                    c += 2 * (m * n) * (x1 * y1)
                    e0 -= 2 * D_main(m, n, x1, y1) * (m * n) / A * (x1 * y1) / A
                    #Top Right
                    c += 2 * (m * n) * ((s - x2) * y1)
                    e0 -= 2 * D_main(m, n, s - x2, y1) * (m * n) / A * ((s - x2) * y1) / A
                    #Bottom Left
                    c += 2 * (m * n) * (x1 * (s - y2))
                    e0 -= 2 * D_main(m, n, x1, s - y2) * (m * n) / A * (x1 * (s - y2)) / A
                    #Bottom Right
                    c += 2 * (m * n) * ((s - x2) * (s - y2))
                    e0 -= 2 * D_main(m, n, s - x2, s - y2) * (m * n) / A * ((s - x2) * (s - y2)) / A
                    #Center
                    c += (m * n) * (m * n)
                    e0 -= E(m, n) * (m * n) / A * (m * n) / A

                    c = float(c)
                    e0 = float(e0)
                    e += e0 * A ** 2 / (A ** 2 - c)

                    num += 1
                    if num % 1 == 0: print num, time.time() - start
    return float(e)

if __name__ == '__main__':
    #print S(4)
    #print Ds(1,1,1,1, n_iter)

    #print T2(1,1,1)
    #print repr(S_sim(7, n_iter))
