from collections import defaultdict
from functools import reduce
from itertools import combinations
from operator import mul

def factorize(n):
    """Factorize the numbers up to n, returning a pair (factorization,
    totient).

    factorization is a dictionary mapping each composite i below n to
    a list of numbers p ** e where p is a prime and e is the exponent
    of p in the factorization of i.

    totient is a list whose i'th element is Euler's totient function
    applied to i (the count of numbers less than i which are coprime
    to i).

        >>> from pprint import pprint
        >>> f, t = factorize(10)
        >>> pprint((dict(f), t))
        ({4: [4], 6: [2, 3], 8: [8], 9: [9], 10: [2, 5]},
         [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4])

    """
    n = n + 1
    f = defaultdict(list)
    t = list(range(n))
    for p in range(2, n):
        if p not in f:
            t[p] = p - 1
            for i in range(p + p, n, p):
                j, k = i, 1
                while j % p == 0:
                    j //= p
                    k *= p
                f[i].append(k)
                t[i] = t[i] * (p - 1) // p
    return f, t

def problem407(n):
    """Generate a sequence whose i'th element is the largest a < i such
    that a**2 == a (mod i), where i runs from 1 to n (inclusive).

    """
    f, t = factorize(n + 1)
    yield 0 # i = 1
    for i in range(2, n + 1):
        if i not in f or len(f[i]) < 2:
            # prime or prime power
            yield 1
            continue
        def uw():
            for j in range(1, len(f[i])):
                for c in combinations(f[i], j):
                    u = reduce(mul, c)
                    v = i // u
                    w = pow(u, t[v] - 1, v)
                    yield u * w
        yield max(uw())

my_sum = 0
for item in problem407(10**6):
    my_sum += item
print my_sum