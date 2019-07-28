from Euler import factor, memoize
from math import sqrt, floor

def geom(a, r, n):
    return int((a*(r**n - 1))/(r-1))

# Return proper divisors of n, along with the max exponent
# of the divisor that is less than n
@memoize
def divisors(n):
    d = []
    limit = int(n**.5)+1
    for x in xrange(2, limit):
        if n % x == 0:
            exp1 = max_exp(n, x)
            if x == (n/x):
                d.append((x, exp1))
            else:
                exp2 = max_exp(n, (n/x))
                d.append((x, exp1))
                d.append((n/x, exp2))
    return d

@memoize
def max_exp(n, d):
    exp = 0
    while n > 0 and n % d == 0:
        n /= d
        exp += 1
    return exp


def s(n):
    ds = divisors(n)

    max_gsum = 0
    for d, exp in ds:
        # Only valid if the progression has 3 or more integers
        if exp > 1:
            gsum = geom(n, (d-1.)/d, exp+1)
            if gsum > max_gsum:
                max_gsum = gsum
    return max_gsum

def S(k):
    return max(s(n) for n in xrange(k+1))

def S2(k):
    vals = [s(n) for n in xrange(k+1)]
    max_val = max(vals)
    max_ind = vals.index(max_val)
    return max_val, max_ind


def validate():
    assert S(4) == 7
    assert S(10) == 19
    assert S(12) == 21
    assert S(1000) == 3439
    assert T(1000) == 2268

def T(n):
    max_s = 0
    s_vals = []
    output = 0
    for k in xrange(4, n+1):
        val = s(k)
        if val > max_s:
            max_s = val

        output += max_s*(-1)**k
    return output

def is_square(val): return floor(sqrt(val)) == sqrt(val)

def main():
    prev_val = False
    for i in range(2, 10000):
        max_val, max_ind = S2(i)
        if max_val != prev_val:
            print i, max_val, max_ind, factor(max_ind), is_square(max_ind)
        prev_val = max_val

if __name__ == '__main__':
    main()
