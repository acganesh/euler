from Euler import prime_sieve
import itertools

primes = prime_sieve(1000000)
primes_set = set(primes)

def main(n):
	for num in primes:
		num = str(num)
		length = len(num)
		
		ind_list = range(length)

		for i in ind_list:
			subsets = itertools.combinations(ind_list, i+1)

			for subset in subsets:
				num_cand = list(num)
				vals = []
				if 0 in subset: a = 1
				else: a = 0
				for digit in range(a, 10):
					for ind in subset:
						num_cand[ind] = str(digit)
					val = int(''.join(num_cand))
					if val in primes_set:
						vals.append(val)

				if len(vals) == n:
					return vals

print main(8)