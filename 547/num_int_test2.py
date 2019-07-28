from scipy.integrate import dblquad, nquad, quad
from math import sqrt, cos, pi, log


def En(a, b):
    a, b = float(a), float(b)
    val = dblquad(lambda x, y: sqrt(x**2+y**2)*(1.-x/a)*(1.-y/b), 0., b, lambda x: 0., lambda x: a)
    return 4/(a*b)*val[0]


def integrand(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

def En2(a, b):
    a, b = float(a), float(b)
    ranges = [(0,a), (0, b)]*2
    print ranges
    prec = {'epsrel': 1e-2, 'epsabs': 1e-2}
    val = nquad(integrand, ranges, opts=prec)
    A = a*b
    return val[0]

def D(m, n, i, j):
    m, n, i, j = map(float, (m, n, i, j))
    ranges = [(0, m), (0, n), (m, m+i), (n, n+j)]
    prec = {'epsrel': 1e-4, 'epsabs': 1e-4}
    val = nquad(integrand, ranges, opts=prec)
    return 1./(m*n*i*j)*val[0]


def Dc(a, b):
    a, b = float(a), float(b)
    d = sqrt(a**2+b**2)
    E = 1./3*(d + b**2/(2*a)*log((a+d)/b) + a**2/(2*b)*log((b+d)/a))
    return E

def integrand2(theta, m, n, i, j):
    v1 = Dc(m, n)
    v2 = Dc(i, j)
    val = sqrt(v1**2 + v2**2 - 2*v1*v2*cos(theta))
    return val

# This doesn't quite work, sadly
# But it's far more efficient, since it's a
# single integral
def D2(m, n, i, j):
    m, n, i, j = map(float, (m, n, i, j))
    args = (m, n, i, j)
    val = quad(integrand2, 0, pi, args=args)
    A = m*n+i*j
    return val[0]

#print En2(1,1)
