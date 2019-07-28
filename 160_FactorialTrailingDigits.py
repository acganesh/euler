def last_k_nonzero(n, k):
	prod = 1
	val = 1
	mod = 10**k
	ctr = 0
	while val <= n:
		prev_val = val
		while val % 5 == 0:
			val /= 5
			ctr += 1
		while ctr > 0:
			if val % 2 == 0:
				val /= 2
				ctr -= 1
			else:
				break

		prod = (prod*val) % mod
		val = prev_val + 1
		#if val % 1000000 == 0: print val
	return prod

for exp in range(1, 10):
	print last_k_nonzero(10**exp, 5)
'''
print last_k_nonzero(10, 5)
print last_k_nonzero(100, 5)
print last_k_nonzero(1000, 5)
print last_k_nonzero(10000, 5)
'''