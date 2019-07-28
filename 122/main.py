from math import log, ceil, floor
from joblib import Parallel, delayed

memo = {}

# m(k, vals=[1])
# = m(k-1, vals=[1, 2])

def m(k, exp=1, vals=[1]):
    #if (k, exp) in memo: return memo[(k, exp)]
    #else:
    return _m(k) - 1

def _m(k, exp=1, vals=[1]):
    #if (k, exp) in memo: return memo[(k, exp)]
    #if k in memo: return memo[k]
    #if k - exp + 1 in memo: return len(vals) - 1 + memo[k-exp+1]

    # Upper bound for minimal length using binary method
    #min_length = int(ceil(2*log(k, 2)))
    min_length = (4./3)*floor(log(k, 2)) + 3
    #min_length = (1.620412)*(log(k, 2)) + 1
    if exp > k:
        return None
    if exp == k:
        return len(vals)
    if min_length != None and len(vals) > min_length:
        return None
    for v in vals:
        new_vals = vals+[exp+v]
        length = _m(k, exp+v, new_vals)
        if min_length is None or length < min_length:
            if length != None:
                min_length = length
                #if (k, exp+v) in memo: memo[(k, exp+v)] = min(memo[(k, exp+v)], length)
                #else: memo[(k, exp+v)] = length

               #memo[k] = min_length

    #memo[k] = min_length
    """
    if k in memo:
        memo[k] = min(memo[k], min_length - 1)
    else:
        memo[k] = min_length - 1
    """
    return min_length

def s_m(lim):
    total = 0
    for k in xrange(1, lim+1):
        if k % 10 == 0:
            print k
        result = m(k)
        #if int(result) != result: print 'failure', result
        total += m(k)
    return total

def s_m_p(lim):
    results = Parallel(n_jobs=8)(delayed(m)(k) for k in xrange(1, lim+1))
    return sum(results)

# Clearly, m(k) == m(k, exp=2, vals=[1,2])
# If you could do memoized recursion, this problem is solved.
print s_m_p(70)
