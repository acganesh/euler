def factor_sieve(n):
	sieve = [[1, k] for k in range(n+1)]
	for x in range(2, n+1):
		if sieve[x][0] == 1:
			for y in range(x, n+1, x):
				sieve[y][0] *= x
	return sieve

def tests():
	print sorted(factor_sieve(10), key = lambda x: x[0])
	print main(10, 4)
	print main(10, 6)

def main(limit, N):
	my_list = sorted(factor_sieve(limit), key = lambda x: x[0])
	return my_list[N][1]

print main(100000, 10000)