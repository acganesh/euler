from Euler import prime_sieve, is_perm, sqrt
 
L = 10**11
primes = prime_sieve(int(1.30*sqrt(L)))
del primes[:int(0.6*len(primes))]

def pe70(limit):
	min_q, min_n, i = 2, 0, 0
	for p1 in primes:
		i+=1
		for p2 in primes[i:]:
			if (p1+p2)%9 != 1: continue
			n = p1 * p2
			if n > limit: return min_n
			phi = (p1-1) * (p2-1)
			q = n / float(phi)
			if is_perm(phi, n) and min_q>q: min_q, min_n = q, n
	return "NFI!"

print "Project Euler 70 Solution =",pe70(L)