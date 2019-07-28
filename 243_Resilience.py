from Euler import prime_sieve, factor
from fractions import Fraction

primes = prime_sieve(100)
prime_set = set(primes)

def totient(n):
	F = factor(n)
	factors = zip(*F)[0]
	val = 1
	for num in factors:
		val *= (num-1)/float(num)
	val *= (n)
	return int(val)

def main(limit):
	n = 1
	for p in primes:
		n *= p
		val = Fraction(totient(n), n-1)
		if val < limit:
			n /= p
			for i in range(2, 100):
				if not i in prime_set:
					val = Fraction(totient(n*i), n*i-1)
					if val < limit:
						return n*i

print main(Fraction(15499, 94744))