#returns exponent of p in prime factorization of n!
def legendre(n, p):
	total = 0
	while n / p > 0:
		total += n / p
		p *= p
	return total

print legendre(200, 5)
def main(n):
	pass
