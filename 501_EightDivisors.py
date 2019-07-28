from Euler import prime_sieve
import itertools

def subsets(S,m):
	return set(itertools.combinations(S,m))


def main(N):
	primes = prime_sieve(N)

	factorizations = [(2,2,2), (4,2), (8,1)]


	length = len(primes)

	vals = set([])

	for a in range(length):
		for b in range(a+1, length):
			val = a**3*b
			if val > N:
				break
			if not (val in vals):
				vals.add(val)

	for a in primes:
		val = a ** 7 
		if val > N:
			break
		if not (val in vals):		
			vals.add(val)


	for a in range(length):
		for b in range(a+1, length):
			for c in range(b+1, length):
				val = primes[a]*primes[b]*primes[c]
				#print val
				if val > N:
					break
				if not (val in vals):
					vals.add(val)

	print len(vals)

for N in range(1, 10):
	main(100*N)






