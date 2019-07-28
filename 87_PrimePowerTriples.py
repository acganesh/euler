from Euler import prime_sieve

primes = prime_sieve(10000)
vals = []
#limit = 50*10**6
limit = 50*10**6

for a in primes:
	if a**4 > limit:
		break
	for b in primes:
		if b**3 > limit:
			break
		for c in primes:
			if c**2 > limit:
				break
			num = a**4 + b**3 + c**2
			if num < limit:
				vals.append(num)

print len(set(vals))