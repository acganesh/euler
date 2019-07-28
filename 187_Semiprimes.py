from math import sqrt, floor

def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

def main(limit):
	#sqrt_limit = int(floor(sqrt(limit)))
	primes = set(primes_sieve(limit))

	my_set = set()
	for prime1 in primes:
		for prime2 in primes:
			#print prime1, prime2
			#print prime1, prime2
			prod = prime1*prime2
			if not prod in my_set and prod < limit:
				my_set.add(prod)

	#print my_set
	return len(my_set), len(primes)

'''
for i in primes1:
	for j in primes1:
		print i, j
'''
print main(50)