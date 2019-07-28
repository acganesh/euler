def factor_sieve(n):
	sieve = [[] for x in range(n+1)]
	for x in range(2, n+1):
		if sieve[x] == []:
			for y in range(x, n+1, x):
				exp = 1
				num = y
				while num % x == 0:
					num //= x
					exp += 1
				sieve[y].append((x, exp-1))
	return sieve

factors = factor_sieve(12000)

def is_product_sum(n):
	fact = factors[n]
	prod = 1
	for item in fact:
