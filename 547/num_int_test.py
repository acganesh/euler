import numpy as np
from math import asin, acos, sqrt

def Pn(a, b):
    def f(x, a=a, b=b):
        x, a, b = map(float, (x, a, b))
        if 0 < x < a:
            val = np.pi/2.
        if a <= x < b:
            val = asin(a / x)
        if b <= x <= sqrt(a**2+b**2):
            val =  asin(a / x) - acos(b / x)
        else:
            val =  0
        return x / (a*b) * val
    dx = 0.1
    vals = np.arange(0, sqrt(a**2+b**2), dx)
    fvals = map(f, vals)
    result = np.trapz(fvals, vals)
    return result

#print Pn(1, 1)


def En(a, b):
    # Density of the E(a, b) case
    def phi(x, a=a, b=b):
        x, a, b = map(float, (x, a, b))
        if 0 <= x < a:
            val = a*b*np.pi/2 - (a+b)*x + x**2/2.
        elif a <= x < b:
            val = a*b*asin(a/x) - a**2/2 - b*sqrt(x**2 - a**2)
        elif b <= x <= sqrt(a**2+b**2):
            val = a*b*(asin(a/x) - asin(sqrt(1 - b**2/x**2)))
            val = val - (a**2+b**2)/2 - x**2/2 + a*sqrt(x**2-b**2) + b*sqrt(x**2 - a**2)
        else:
            val = 0
        return float(4*x/(a**2*b**2)*val)

    def phi2(l, a=a, b=b):
        l, a, b = map(float, (l, a, b))
        if 0 <= l < a:
            val = a*b*np.pi/2 - a*l - b*l + l**2/2.
        elif a <= l <= b:
            val = a*b*asin(a/l) + b*(l**2-a**2)**.5 - b*l - a**2/2
        else:
            val = 0
        return 4*l/(a**2*b**2)*val

    a = float(a)
    b = float(b)
    dx = 0.001
    vals = np.arange(0.0, sqrt(a**2+b**2), dx)
    fvals = map(phi2, vals)
    result = np.trapz(fvals, vals)
    return result


print En(1,1)

