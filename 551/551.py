from math import log
def main(N):
    return N*log(N)/(2.*log(2))

def main2(N):
    return N**2/(100)*log(N)/log(10)

def digsum(N):
    N_str = str(N)
    return sum(map(int, list(N_str)))

memo = {}
def f(N):
    if N in memo:
        return memo[N]
    if N == 0:
        val = 1
        memo[N] = val
        return val
    if N == 1:
        val = 1
        memo[N] = val
        return val
    else:
        val = sum((digsum(f(i)) for i in xrange(N)))
        #prev = f(N-1); print prev
        #val = digsum(prev) + prev
        #val = digsum(f(N-1)) + f(N-1)
        memo[N] = val
        return val

#print f(10)
print f(999)
print f(1000)
#print f(9999)
#print f(10000)
#print f(100000)

