#return exponent of p in prime factorization of n
def num_factors(n, p):
	num = 0
	if n % p == 0:
		num += 1
		p *= p
	return num

#returns exponent of p in prime factorization of n!
def legendre(n, p):
	total = 0
	while n / p > 0:
		total += n / p
		p *= p
	return total

def main(limit, p):
	total = 0
	for n in range(limit):
		for k in range(n):
			if legendre(n, p) - legendre(n-k, p) - legendre(k, p) == 0:
				total += 1
	return total + limit

p = 7
#print main(100, p)

for N in range(1, 100):
	print N, main(N, p)
