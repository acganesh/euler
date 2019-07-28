from Euler import prime_sieve, is_prime
import itertools

primes = prime_sieve(70)
prime_set = set(primes)

def is_prime_set(vals):
	subsets = itertools.combinations(vals, 2)
	failed_set = set([])
	for a, b in subsets:
		a = str(a); b = str(b)
		str1 = a+b
		str2 = b+a
		if not is_prime(int(str1)) or not is_prime(int(str2)):
			return False
	return True

def main():
	d = {}
	subsets = itertools.combinations(primes, 3)
	for s in subsets:
		if is_prime_set(s):
			print s
			if s[0] in d:
				d[s[0]].append(s)
			else:
				d[s[0]] = [s]


main()

print is_prime_set([3,7,109,673])