from fractions import Fraction

# Akiyama-Tanigawa algorithm for Bernoulli_n
def bernoulli(n):
    A = [0]*(n+1)
    for m in xrange(n+1):
        A[m] = Fraction(1, (m+1))
        for j in xrange(m, 0, -1):
            A[j-1] = j*(A[j-1] - A[j])
    return A[0]

# Naive implementation of Bernoulli denominator
def D(n):
    return bernoulli(n).denominator
