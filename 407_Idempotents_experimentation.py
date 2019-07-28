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

def subsets(arr):
    """ Note this only returns non empty subsets of arr"""
    return chain(*[combinations(arr,i + 1) for i,a in enumerate(arr)])

def k_subset(arr, k):
    s_arr = sorted(arr)
    return set([i for i in combinations(subsets(arr),k) 
               if sorted(chain(*i)) == s_arr])

#Knuth's algorithm - has a bug
def algorithm_u(ns, m):
    def visit(n, a):
        ps = [[] for i in xrange(m)]
        for j in xrange(n):
            ps[a[j + 1]].append(ns[j])
        return ps

    def f(mu, nu, sigma, n, a):
        if mu == 2:
            yield visit(n, a)
        else:
            for v in f(mu - 1, nu - 1, (mu + sigma) % 2, n, a):
                yield v
        if nu == mu + 1:
            a[mu] = mu - 1
            yield visit(n, a)
            while a[nu] > 0:
                a[nu] = a[nu] - 1
                yield visit(n, a)
        elif nu > mu + 1:
            if (mu + sigma) % 2 == 1:
                a[nu - 1] = mu - 1
            else:
                a[mu] = mu - 1
            if (a[nu] + sigma) % 2 == 1:
                for v in b(mu, nu - 1, 0, n, a):
                    yield v
            else:
                for v in f(mu, nu - 1, 0, n, a):
                    yield v
            while a[nu] > 0:
                a[nu] = a[nu] - 1
                if (a[nu] + sigma) % 2 == 1:
                    for v in b(mu, nu - 1, 0, n, a):
                        yield v
                else:
                    for v in f(mu, nu - 1, 0, n, a):
                        yield v

    def b(mu, nu, sigma, n, a):
        if nu == mu + 1:
            while a[nu] < mu - 1:
                visit(n, a)
                a[nu] = a[nu] + 1
            visit(n, a)
            a[mu] = 0
        elif nu > mu + 1:
            if (a[nu] + sigma) % 2 == 1:
                for v in f(mu, nu - 1, 0, n, a):
                    yield v
            else:
                for v in b(mu, nu - 1, 0, n, a):
                    yield v
            while a[nu] < mu - 1:
                a[nu] = a[nu] + 1
                if (a[nu] + sigma) % 2 == 1:
                    for v in f(mu, nu - 1, 0, n, a):
                        yield v
                else:
                    for v in b(mu, nu - 1, 0, n, a):
                        yield v
            if (mu + sigma) % 2 == 1:
                a[nu - 1] = 0
            else:
                a[mu] = 0
        if mu == 2:
            visit(n, a)
        else:
            for v in b(mu - 1, nu - 1, (mu + sigma) % 2, n, a):
                yield v

    n = len(ns)
    a = [0] * (n + 1)
    for j in xrange(1, m + 1):
        a[n - m + j] = j - 1
    return f(m, n, 0, n, a)

#print k_subset([1,2,3,4,5], 2)

start = datetime.datetime.now()

def phi(n):
    amount = 0

    for k in range(1, n + 1):
        if gcd(n, k) == 1:
            amount += 1

    return amount
#works if gcd(u,v) = 1
def modinv_cp(u,v):
	return (u ** (phi(v) - 1)) % v

def list_partition(l, K):
	for splits in combinations(range(len(l)-1), K-1):
		splits = [0] + [s + 1 for s in splits] + [None]
		yield [l[s:e] for s, e in zip(splits, splits[1:])]


for item in list_partition([1,2,3,4,5], 2):
	print item

def Primes(a):
    sieve=[True]*(a+1)
    sieve[:2]=[False, False]
    sqrt=int(a**.5)+1
    for x in range(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(a/x-1)
    return sieve

def factorSieve2(a):
    p=Primes(a)
    sieve=[[] for x in range(a+1)]
    for x in range(2,a):
        if p[x]:
            for z in range(x, a+1, x):
                sieve[z].append(x)
    return sieve
#print factorSieve2(200000)

def factor_sieve3(n):
	n = n+1
	f = defaultdict(list)
	t = list(range(n))
	for p in range(2, n):
		if p not in f:
			t[p] = p-1
			for i in range(p+p, n, p):
				j, k = i, 1
				while j % p == 0:
					j //= p
					k *= p
				f[i].append(k)
				t[i] = t[i] * (p-1) // p
	return f, t

def coprime_decomposition(factors, n):
	decomps = []
	for prime in factors:
		exp = 1
		while prime ** exp < n:
			exp += 1
		decomps.append((prime, exp-1))
	return decomps
#print factor_sieve3(10)

def k_subset_2(s, k):
    if k == len(s):
        return (tuple([(x,) for x in s]),)
    k_subs = []
    for i in range(len(s)):
        partials = k_subset(s[:i] + s[i + 1:], k)
        for partial in partials:
            for p in range(len(partial)):
                k_subs.append(partial[:p] + (partial[p] + (s[i],),) + partial[p + 1:])
    return k_subs

def uniq_subsets(s):
    u = set()
    for x in s:
        t = []
        for y in x:
            y = list(y)
            y.sort()
            t.append(tuple(y))
        t.sort()
        u.add(tuple(t))
    return u

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

print factor_sieve(20)

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
			#print 'one_prime',factors[num]
			#print 'M',num,1
			my_sum += 1
		else:
			#partitions = list_partition(factors[num], 2)
			#partitions = k_subset(factors[num], 2)
			#partitions = algorithm_u(factors[num], 2)
			#partitions = uniq_subsets(k_subset_2(factors[num], 2))
			partitions = neclusters(factors[num], 2)
			ctr = 1
			max_uw = 0
			
			is_list = False
			generator = True

			if is_list:
				for pairs in partitions:
					if num == 70:
						print pairs
					u_pairs, v_pairs = pairs[0], pairs[1]
					#if num == 30: import pdb; pdb.set_trace()
					u, v = 1, 1

					#print 'u',u_pairs
					#print 'v',v_pairs
					for pair in u_pairs:
						#print pair
						u *= (pair[0] ** pair[1])
					for pair in v_pairs:
						v *= (pair[0] ** pair[1])

					if num == 30:
						print u, v

					#print 'u','v',u,v
					w1 = pow(u,t[v] - 1,v)
					w2 = pow(v,t[u] - 1,u)

					#w1 = modinv_cp(u, v)
					#w2 = modinv_cp(v, u)
					#print 'w',w1, w2
					max_uw = max(max_uw, u*w1, v*w2)
			
			if generator:
				while True:
					try:
						pairs = partitions.next()
						if num == 70:
							print pairs
						u_pairs, v_pairs = pairs[0], pairs[1]
						#if num == 30: import pdb; pdb.set_trace()
						'''
						for pairs in pair_set:
							#print 'pairs',pairs
							if ctr == 1: 
								u_pairs = pairs
							elif ctr == 2:
								v_pairs = pairs
							ctr += 1
						'''
						u, v = 1, 1

						#print 'u',u_pairs
						#print 'v',v_pairs
						for pair in u_pairs:
							#print pair
							u *= (pair[0] ** pair[1])
						for pair in v_pairs:
							v *= (pair[0] ** pair[1])

						if num == 30:
							print u, v

						#print 'u','v',u,v
						w1 = pow(u,t[v] - 1,v)
						w2 = pow(v,t[u] - 1,u)

						#w1 = modinv_cp(u, v)
						#w2 = modinv_cp(v, u)
						#print 'w',w1, w2
						max_uw = max(max_uw, u*w1, v*w2)
					except StopIteration:
						break
				
			
			if num == 70: print 'M', num, max_uw

			my_sum += max_uw
		num += 1
		#if num % 10000 == 0: print num
	print 'sum', my_sum

main(N)







#print factor_sieve(50)

#u, v factorizations
#




def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m





def test(n):
	x = n-1
	while x > 0:
		u = gcd(n, x)
		v = gcd(n, x-1)
		w = x/u
		if modinv_cp(u, v) == w:
			return x
		x -= 1

#print test(6)

def max_idempotent(n):
	a = n-1
	while a > 0:
		gcd_val = gcd(n, a)
		if a % (n/gcd_val) == 1:
			return a
		a -= 1

#for item in range(40):
	#print 'MI', item, max_idempotent(item)
limit = 1000
ctr = 2
my_sum = 0

while ctr < 10:
	val = max_idempotent(ctr)
	if ctr == 70: print ctr,val
	my_sum += val
	ctr += 1
	if ctr % 1000 == 0:
		print ctr

print my_sum

print datetime.datetime.now() - start

#print max_idempotent(6)
