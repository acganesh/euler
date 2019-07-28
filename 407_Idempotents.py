from fractions import gcd
import datetime
from collections import defaultdict
from functools import reduce
from itertools import chain, combinations
from operator import mul
from Euler import prime_sieve
import itertools

def clusters(l, K):
    if l:
        prev = None
        for t in clusters(l[1:], K):
            tup = sorted(t)
            if tup != prev:
                prev = tup
                for i in xrange(K):
                    yield tup[:i] + [[l[0]] + tup[i],] + tup[i+1:]
    else:
        yield [[] for _ in xrange(K)]

def neclusters(l, K):
    for c in clusters(l, K):
        if all(x for x in c): yield c

start = datetime.datetime.now()

def factor_sieve(n):
	t = list(range(n+1))
	sieve = [[] for x in range(n+1)]
	for x in range(2, n+1):
		if sieve[x] == []:
			t[x] = x-1
			for y in range(x, n+1, x):
				exp = 1
				num = y
				while num % x == 0:
					num //= x
					exp += 1
				sieve[y].append((x, exp-1))
				if y != x:
					t[y] = t[y]*(x-1) // x
	return sieve, t

N = 10**7
def main(N):
	N = N+1
	factors,t = factor_sieve(N)

	num = 2
	my_sum = 0
	u_pairs = []
	v_pairs = []
	while num < N:
		if len(factors[num]) == 1:
			my_sum += 1
		else:
			partitions = neclusters(factors[num], 2)
			ctr = 1
			max_uw = 0
			
			while True:
				try:
					pairs = partitions.next()
					u_pairs, v_pairs = pairs[0], pairs[1]
					u, v = 1, 1

					for pair in u_pairs:
						u *= (pair[0] ** pair[1])
					for pair in v_pairs:
						v *= (pair[0] ** pair[1])

					w1 = pow(u,t[v] - 1,v)
					w2 = pow(v,t[u] - 1,u)

					max_uw = max(max_uw, u*w1, v*w2)
				except StopIteration:
					break
				
			my_sum += max_uw
		num += 1
		#if num % 10000 == 0: print num
	print 'sum', my_sum


main(10**7)


print datetime.datetime.now() - start

#print max_idempotent(6)
