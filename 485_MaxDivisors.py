'''
Let d(n) be the number of divisors of n.
Let M(n,k) be the maximum value of d(j) for n ≤ j ≤ n+k-1.
Let S(u,k) be the sum of M(n,k) for 1 ≤ n ≤ u-k+1.

You are given that S(1000,10)=17176.

Find S(100 000 000,100 000).
'''
from Euler import factor
import datetime

start = datetime.datetime.now()

cache = [-1] * 10000000


def d(n):
	div_cache = cache[n]
	if div_cache != -1:
		return div_cache
	else:
		factorization = factor(n)
		div = 1
		for val in factorization:
			div *= (val[1]+1)
		cache[n] = div
		return div

def M(n, k, give_ind = False):
	j = n
	max_val = 0
	ind = 0
	while j <= n+k-1:
		val = d(j)
		if val > max_val:
			ind = j
			max_val = val
		j += 1
	if give_ind:
		return max_val, ind
	else: 
		return max_val

def S2(u, k):
	total = 0
	n = 1
	while n <= u-k+1:
		if n > 1:
			if ind != (n-1):
				val = max(val, d(n+k-1))
				print 'done'
			else:
				val, ind = M(n, k, True)
		else:
			val, ind = M(n, k, True)
		total += val
		n += 1
	return total


def S(u, k):
	total = 0
	n = 1
	while n <= u-k+1:
		total += M(n, k)
		n += 1
	return total

print S2(10000, 100)
#print S(1000, 10)
#print S(100000, 1000)
#print M(1000, 10)

#print d(24)

print datetime.datetime.now() - start

def main(n):
	pass
