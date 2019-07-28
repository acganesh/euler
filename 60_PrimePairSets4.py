'''
0,1,1,1
The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any 
order the result will always be prime. For example, 
taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the 
lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

5th_num = odd
has to be 1 mod 3.
'''

from math import sqrt
from Euler import prime_sieve

def isPrime(n):
	bound = sqrt(n)
	divisors = []

	i = 2
	while i <= bound:
		if (n % i) == 0:
			return False
		i += 1
	return True

def is_5_tuple_prime_set(n):
	candidates = []
	four_primes = [3,7,109,673]

	for item in four_primes:
		a = int(str(n)+str(item))
		b = int(str(item)+str(n))

		candidates.append(a)
		candidates.append(b)

	for item in candidates:
		if isPrime(item) == False:
			return False
	return True

def is_4_tuple_prime_set(n):
	candidates = []
	four_primes = [3,7,109]

	for item in four_primes:
		a = int(str(n)+str(item))
		b = int(str(item)+str(n))

		candidates.append(a)
		candidates.append(b)

	for item in candidates:
		if isPrime(item) == False:
			return False
	return True

print is_4_tuple_prime_set(2)

n = 1
limit = 10 ** 8
ctr = 0
primes = prime_sieve(limit)

for n in primes:
	if is_5_tuple_prime_set(n):
		print "Answer: "+str(n)
		break
	ctr += 1
	if ctr % 10000 == 0:
		print ctr

