# http://code.activestate.com/recipes/578231-probably-the-fastest-memoization-decorator-in-the-/
def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)

@memoize
def f(k, n):
    if n < k: return n+1
    return sum(f(k, i/k) for i in xrange(n+1))

@memoize
def f0(k, n):
    if n < k: return n+1
    return f0(k, n-1) + f0(k, n/k)

# Using notation from
# http://www.sciencedirect.com/science/article/pii/S0012365X03000967
mem = {}
def f2(m, n, k=1):
    if (m, n) in mem:
        return mem[(m, n)]
    if n == 1: return k+1
    if k == 0: return 1

    a = f2(m, n, k-1) + f2(m, n-1, k*m)
    mem[(m, n)] = a
    return a


def tests(functions):
    for f in functions:
        assert f(5, 10) == 18
        assert f(7, 100) == 1003
        assert f(2, 1000) == 264830889564


#tests([f])
for i in range(1, 10):
    print f0(2, i)
#print f0(2, 10**6)
#print f2(10, 10**5)

