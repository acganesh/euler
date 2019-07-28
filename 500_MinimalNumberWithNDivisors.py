from Euler import factor, prime_sieve

mod = 500500507
primes = prime_sieve(8000000)
my_list = []

for x in primes:
	exp = 1
	while exp <= 4:
		val = x**(2**exp)
		my_list += [val]
		if val > 8000000: #pretty close to the 500500th prime
			break
		exp += 1

combined = primes + my_list
combined.sort()
combined_m = [x % mod for x in combined]

def main(N):
	exp = 1
	val = 2
	mod = 500500507	
	while exp < N:
		val *= combined_m[exp]
		val = val % mod
		exp += 1
		#if exp % 10000 == 0: print exp
	return val % mod

print main(500500)

def testing():
	def product(my_list):
		prod = 1
		for item in my_list:
			prod *= item
		return prod

	def brute_force(num_div):
		n = 1
		while True:
			factorization = factor(n)
			#print factorization
			num_factors = product([(x[1]+1) for x in factorization])
			#print num_factors
			if num_factors == num_div:
				return num
			n += 1
	def main_not_modded(N):
		exp = 1
		val = 2
		mod = 500500507	
		while exp < N:
			val *= combined[exp]
			val = val
			exp += 1
			#if exp % 10000 == 0: print exp
		return val





