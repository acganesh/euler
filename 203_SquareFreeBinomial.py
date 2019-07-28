from Euler import prime_sieve
from scipy.special import binom

def tests():
	print main(8)
#returns the exponent of p in n!
def num_primes(p, n):
	total = 0
	while n > 1:
		n /= p
		total += n
	return total

#checks if the binomial coefficient nCk is squarefree
def is_squarefree(n, k):
	primes = prime_sieve(n)
	for p in primes:
		num = num_primes(p, n) - num_primes(p, k) - num_primes(p, n-k)
		if num >= 2:
			return False
	return True

def main(num_rows):
	squarefree_set = set([])
	total = 1 #1 is counted as squarefree
	for a in range(1, num_rows):
		for b in range(1, a):
			if is_squarefree(a,b):
				val = binom(a,b)
				if val not in squarefree_set:
					total += val
					squarefree_set.add(val)
	return int(total)

print main(51)


