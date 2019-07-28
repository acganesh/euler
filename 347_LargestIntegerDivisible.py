from Euler import prime_sieve

def M(p, q, N):
	primes  = prime_sieve(N)
	for p in primes:
		gen = (x for x in primes if x != p)
		for q in gen:
			while num1