# Script to test frequency distributions
# and implement combinatorial algorithm

from collections import Counter, defaultdict
from itertools import product
from joblib import Parallel, delayed

def factor_sieve(n):
    sieve = Counter()
    for x in xrange(2, n+1):
        if sieve[x] == 0:
            for y in xrange(x, n+1, x):
                exp = 1
                num = y
                while num % x == 0:
                    num //= x
                    exp += 1
                sieve[y] += (exp - 1)
    return sieve

fs = factor_sieve(10**5)
memo = {}

def F(*args):
    s_args = tuple(sorted(args))
    #if s_args in memo: return memo[s_args]
    freqs = Counter()
    for arg in args:
        freq = fs[arg]
        freqs[freq] += 1
    for k in freqs.keys():
        if k != 1 and freqs[k] % 2 == 1:
            val = 1
            memo[s_args] = val
            return freqs, val
    val = 2
    memo[s_args] = val
    return freqs, val

def F_p(*args):
    s_args = tuple(sorted(args))
    if s_args in memo: return memo[s_args]
    freqs = Counter()
    for arg in args:
        freq = fs[arg]
        freqs[freq] += 1
    for k in freqs.keys():
        if k != 1 and freqs[k] % 2 == 1:
            val = 1
            memo[s_args] = val
            return val
    val = 0
    memo[s_args] = val
    return val

def parse_freq_dist(f):
    S_2 = 0
    S_3 = 0
    S_c = 0
    for key in f.keys():
        if len(key) > 1:
            vals = sorted(zip(*key)[0])
        else:
            vals = key[0][0]
        if vals == 1 or vals == 2 or vals == [1, 2]:
            S_2 += f[key]
        elif vals == [1, 3] or vals == 3:
            S_3 += f[key]
        else:
            S_c += f[key]
    return S_2, S_3, S_c


def old_main(n, k):
    total = 0
    #freq_dist = defaultdict(dict)
    freq_dist = Counter()
    for args in product(xrange(2, n+1), repeat=k):
        freqs, val = F(*args)
        if val == 2:
            #print args, tuple(sorted(freqs.iteritems()))
            freq_dist[tuple(sorted(freqs.iteritems()))] += 1
        else: total += 1
    #print 'freq_dist', freq_dist
    # sums = parse_freq_dist(freq_dist)
    #print 'sums: ', sums
    return total

def old_main2(n, k):
    total2 = 0
    #freq_dist = defaultdict(dict)
    freq_dist = Counter()
    for args in product(xrange(2, n+1), repeat=k):
        freqs, val = F(*args)
        if val == 2:
            #print args, tuple(sorted(freqs.iteritems()))
            total2 += 1
            freq_dist[tuple(sorted(freqs.iteritems()))] += 1
    total = (n-1)**k
    return total - total2

# This is slower
def parallel_main(n, k):
    results = Parallel(n_jobs=8)(delayed(F_p)(*i) for i in product(xrange(2, n+1), repeat=k))
    return sum(results)


def test_prod(n, k):
    for args in product(xrange(2, n+1), repeat=k):
        print args

def main_with_vals(n, k):
    total = 0
    freq_dist = Counter()
    vals = defaultdict(list)
    for args in product(xrange(2, n+1), repeat=k):
        freqs, val = F(*args)
        if val == 2:
            freq_dist[tuple(sorted(freqs.iteritems()))] += 1
            vals[tuple(sorted(freqs.iteritems()))].append(args)
        else:
            total += 1
    return total

if __name__ == '__main__':
    #print parallel_main(10, 5)
    #print old_main(20, 5)
    #for k in xrange(2, 6): print old_main2(10, k), old_main(10, k)
    main_with_vals(6, 3)
    #print old_main(20, 5)
    """ Diffs between consecutive values
    n = 11
    est = 0
    for k in xrange(2, 20):
        val = main(n, k)
        print val, val-est
    est = (n-1)*val
    """
