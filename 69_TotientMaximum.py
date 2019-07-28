def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return factors

def totient(n):
	factors = set(prime_factors(n))
	#print factors
	prod = 1
	for factor in factors:
		prod *= (1.0 - 1.0/(float(factor)))

	prod *= n

	return prod

n = 2
my_max = 0
max_n = 0

while n <= 1000000:
	ratio = n/totient(n)
	if ratio > my_max:
		my_max = ratio
		max_n = n
	n += 1

	if n % 100000 == 0: print "Iterations: %i" % n

print my_max, max_n