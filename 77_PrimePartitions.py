from Euler import factor

#from http://math.stackexchange.com/a/89661

def factor_sum_sieve(n):
	sieve = [0]*(n+1)
	for x in range(2, n+1):
		if sieve[x] == 0:
			for y in range(x, n+1, x):
				sieve[y] += x
	return sieve

cache = [0]*(10000)
def prime_partitions(n, factor_sums):
	if cache[n] == 0: 
		total = 0
		for j in range(2, n-1):
			total += factor_sums[j]*prime_partitions(n-j, factor_sums)
		total += factor_sums[n]
		total /= n
		cache[n] = total
		return total
	else:
		return cache[n]

def main(n, limit):
	factor_sums = factor_sum_sieve(n)
	for m in range(1, n+1):
		val = prime_partitions(m, factor_sums)
		if val > limit:
			return m, val

print main(100, 5000)